import sqlite3
import hmac
import hashlib

def verificar_senha(senha_fornecida: str, hash_armazenado: str, salt: bytes) -> bool:
    """Verifica a senha usando PBKDF2 em tempo constante."""
    hash_calculado = hashlib.pbkdf2_hmac(
        'sha256',
        senha_fornecida.encode('utf-8'),
        salt,
        iterations=100_000
    ).hex()
    return hmac.compare_digest(hash_calculado, hash_armazenado)

def fazer_login(usuario: str, senha: str) -> str:
    """
    Realiza a autenticação de forma segura:
    1. Utiliza consultas parametrizadas (Prepared Statements) para prevenir SQL Injection.
    2. Utiliza context manager para fechamento seguro dos recursos.
    3. Valida credenciais comparando hashes criptográficos com salt.
    """
    with sqlite3.connect('banco_de_dados.db') as conexao:
        cursor = conexao.cursor()

        # Consulta parametrizada com placeholder '?'
        query = "SELECT password_hash, salt FROM usuarios WHERE username = ?"
        cursor.execute(query, (usuario,))
        resultado = cursor.fetchone()

    if resultado:
        hash_armazenado, salt = resultado
        if isinstance(salt, str):
            salt = bytes.fromhex(salt)

        if verificar_senha(senha, hash_armazenado, salt):
            return "Acesso Permitido!"

    return "Acesso Negado."
