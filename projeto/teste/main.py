import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class TelaInicial(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mãe Águia")
        self.setGeometry(200, 200, 500, 600)

        # Layout principal
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Cabeçalho
        cabecalho = QLabel(" Associação da Mãe Águia")
        cabecalho.setFont(QFont("Arial", 20, QFont.Bold))
        cabecalho.setAlignment(Qt.AlignCenter)
        layout.addWidget(cabecalho)

        descricao = QLabel(
            "Bem-vindo colaborador\n"
            "Aqui você trabalha em pró da familia\n"
        )
        descricao.setFont(QFont("Arial", 12))
        descricao.setAlignment(Qt.AlignCenter)
        layout.addWidget(descricao)

        # Imagem ilustrativa
        imagem = QLabel()
        pixmap = QPixmap()
        pixmap.loadFromData(self.baixar_imagem( 'https://images.vexels.com/media/users/3/276346/isolated/lists/7fa6f3da3f76ce93766da46fc8667df7-elemento-desenhado-a-mao-de-aguia-americana.png'  ))
        pixmap = pixmap.scaled(300, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        imagem.setPixmap(pixmap)
        imagem.setAlignment(Qt.AlignCenter)
        layout.addWidget(imagem)

        # Botão de ação
        botao = QPushButton("Login")
        botao.setStyleSheet(
            "background-color: #2563eb; color: white; font-size: 14px; "
            "padding: 10px; border-radius: 8px;"
        )
        botao.clicked.connect(self.login)
        layout.addWidget(botao)

        self.setLayout(layout)

    def login(self):
        print("logado")

    def baixar_imagem(self, url):
        """Baixa imagem da internet (necessário requests)."""
        import requests
        resposta = requests.get(url)
        return resposta.content


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = TelaInicial()
    janela.show()
    sys.exit(app.exec_())