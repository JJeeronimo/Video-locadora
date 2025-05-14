import random
from datetime import datetime, timedelta

class Cliente:
    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self.telefone = self.formatar_telefone(telefone)
        self.filmes_locados = {}

    def __str__(self):
        locacoes = ', '.join([f"{filme} (Devolver até {data})" for filme, data in self.filmes_locados.items()])
        return f"ID: {self.id}, Nome: {self.nome}, Telefone: {self.telefone}, Filmes Locados: {locacoes if locacoes else 'Nenhum'}"

    @staticmethod
    def formatar_telefone(telefone):
        """ Formata o telefone para o estilo (XX) XXXXX-XXXX """
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"


class Filme:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.disponivel = True

    def __str__(self):
        status = "✅ Disponível" if self.disponivel else "❌ Indisponível"
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Status: {status}"


class Locadora:
    def __init__(self):
        self.clientes = []
        self.filmes = []
        self.ids_gerados = set()
        self.carregar_filmes_padrao()

    def carregar_filmes_padrao(self):
        """ Adiciona filmes predefinidos à locadora """
        filmes_padrao = [
            ("O Chamado", "Terror"), ("Invocação do Mal", "Terror"),
            ("Halloween", "Terror"), ("A Hora do Pesadelo", "Terror"),
            ("Hereditário", "Terror"), ("John Wick", "Ação"),
            ("Mad Max: Estrada da Fúria", "Ação"), ("Velozes e Furiosos", "Ação"),
            ("Gladiador", "Ação"), ("Missão Impossível", "Ação"),
            ("O Poderoso Chefão", "Drama"), ("Forrest Gump", "Drama"),
            ("Clube da Luta", "Drama"), ("A Rede Social", "Drama"),
            ("A Vida é Bela", "Drama"), ("Diário de Uma Paixão", "Romance"),
            ("Titanic", "Romance"), ("Orgulho e Preconceito", "Romance"),
            ("Simplesmente Acontece", "Romance"), ("PS: Eu Te Amo", "Romance"),
            ("Interestelar", "Ficção Científica"), ("Blade Runner 2049", "Ficção Científica"),
            ("A Origem", "Ficção Científica"), ("O Exterminador do Futuro", "Ficção Científica"),
            ("Matrix", "Ficção Científica")
        ]

        for nome, categoria in filmes_padrao:
            self.filmes.append(Filme(nome, categoria))

    def gerar_id_unico(self):
        while True:
            novo_id = random.randint(10000, 99999)
            if novo_id not in self.ids_gerados:
                self.ids_gerados.add(novo_id)
                return novo_id

    def validar_telefone(self, telefone):
        return telefone.isdigit() and len(telefone) == 11

    def cadastrar_cliente(self):
        print("\n=== 🆕 Cadastro de Cliente ===")
        id = self.gerar_id_unico()
        nome = input("Digite o nome do cliente: ").strip()

        while True:
            telefone = input("Digite o telefone do cliente (apenas números, 11 dígitos): ").strip()
            if self.validar_telefone(telefone):
                telefone_formatado = Cliente.formatar_telefone(telefone)
                print(f"\n📞 Telefone formatado: {telefone_formatado}")
                break
            else:
                print("\n⚠️ Telefone inválido! Digite exatamente 11 números.\n")

        cliente = Cliente(id, nome, telefone)
        self.clientes.append(cliente)
        print(f"\n✅ Cliente '{nome}' cadastrado com sucesso! ID: {id}, Telefone: {telefone_formatado}\n")

    def cadastrar_filme(self):
        print("\n=== 🆕 Cadastro de Filme ===")
        nome = input("Digite o nome do filme: ").strip()
        categoria = input("Digite a categoria do filme: ").strip()

        novo_filme = Filme(nome, categoria)
        self.filmes.append(novo_filme)
        print(f"\n✅ Filme '{nome}' cadastrado com sucesso na categoria '{categoria}'!\n")

    def listar_clientes(self):
        print("\n=== 🧑 Lista de Clientes ===")
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        for cliente in self.clientes:
            print(cliente)

    def listar_filmes(self):
        print("\n=== 🎬 Lista de Filmes 🎬 ===")
        if not self.filmes:
            print("Nenhum filme cadastrado.")
        for filme in self.filmes:
            print(filme)

    def locar_filme(self):
        print("\n=== 📽️ Locação de Filme ===")
        nome_cliente = input("Digite o nome do cliente que deseja locar um filme: ").strip().lower()
        cliente = next((c for c in self.clientes if c.nome.lower() == nome_cliente), None)

        if cliente is None:
            print("\n⚠️ Cliente não encontrado! Verifique o nome e tente novamente.\n")
            return

        nome_filme = input("Digite o nome do filme que deseja locar: ").strip().lower()
        filme = next((f for f in self.filmes if f.nome.lower() == nome_filme), None)

        if filme is None or not filme.disponivel:
            print("\n⚠️ Filme não encontrado ou indisponível!\n")
            return
        
        data_devolucao = (datetime.now() + timedelta(days=5)).strftime("%d/%m/%Y")
        cliente.filmes_locados[filme.nome] = data_devolucao
        filme.disponivel = False

        print(f"\n🎉 Filme '{filme.nome}' locado com sucesso para '{cliente.nome}'! Deve ser devolvido até {data_devolucao}.\n")


locadora = Locadora()

while True:
    print("\n=====================================")
    print("     🎬 LOCADORA DE FILMES 🎬      ")
    print("=====================================")
    print("1️⃣ - Cadastrar Cliente")
    print("2️⃣ - Listar Clientes")
    print("3️⃣ - Listar Filmes")
    print("4️⃣ - Locar Filme")
    print("5️⃣ - Devolver Filme")
    print("6️⃣ - Cadastrar Filme")   
    print("7️⃣ - Sair")  
    print("=====================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        locadora.cadastrar_cliente()
    elif opcao == "2":
        locadora.listar_clientes()
    elif opcao == "3":
        locadora.listar_filmes()
    elif opcao == "4":
        locadora.locar_filme()
    elif opcao == "5":
        locadora.devolver_filme()
    elif opcao == "6":
        locadora.cadastrar_filme()
    elif opcao == "7":
        print("\n🚪 Saindo... Obrigado por usar a locadora!\n")
        break
    else:
        print("\n⚠️ Opção inválida! Tente novamente.\n")
