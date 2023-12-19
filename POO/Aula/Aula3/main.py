from inicializador_bd import InicializadorBD
from usuario_repositorio import UsuarioRepositorio
from usuario import Usuario

DB_NAME = "POO/Aula/Aula3/exemplo.sqlite"
InicializadorBD.criar_tabelas(DB_NAME)

usuario_repositorio = UsuarioRepositorio(DB_NAME)

usuario1 = Usuario("Abner Eger", "abner.juda.eger.santana@gmail.com")

try:
    usuario_repositorio.inserir_usuario(usuario1)
except:
    print("E-mail já cadastrado")

# usuarios = usuario_repositorio.obter_usuarios()
# usuario1 = usuarios[0]
# usuario1.nome = "Outro nome"
# usuario1.email = "teste@gmail.com"

# usuario_repositorio.atualizar_usuario(usuario1)

# usuario_repositorio.remover_usuario(usuario1)
