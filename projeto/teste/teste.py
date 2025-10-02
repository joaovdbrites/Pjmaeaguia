import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QCheckBox, QFrame)
from PyQt5.QtGui import QPixmap, QFont, QPalette, QColor
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtSvg import QSvgWidget

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mãe Águia - Sistema de Controle de Atendimentos")
        self.setGeometry(100, 100, 500, 800)
        self.setStyleSheet("""
            QWidget {
                font-family: Arial, sans-serif;
            }
            QPushButton {
                border: none;
                padding: 12px;
                border-radius: 8px;
                font-size: 18px;
            }
            QLineEdit {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 16px;
            }
            QCheckBox {
                spacing: 5px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
        """)
        
        self.initUI()
        
    def initUI(self):
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Cabeçalho
        header = QWidget()
        header.setFixedHeight(150)
        header.setStyleSheet("background-color: #1e40af; color: white;")
        header_layout = QVBoxLayout()
        header_layout.setAlignment(Qt.AlignCenter)
        
        title = QLabel("Associação Mãe Águia")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        subtitle = QLabel("Sistema de Controle de Atendimentos")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 16px;")
        
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        header.setLayout(header_layout)
        
        # Corpo do login
        body = QWidget()
        body_layout = QVBoxLayout()
        body_layout.setAlignment(Qt.AlignCenter)
        body_layout.setSpacing(20)
        body_layout.setContentsMargins(30, 30, 30, 30)
        
        # Título de boas-vindas
        welcome = QLabel("Bem-vindo, colaborador!")
        welcome.setAlignment(Qt.AlignCenter)
        welcome.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        desc = QLabel("Aqui você trabalha em pró da família")
        desc.setAlignment(Qt.AlignCenter)
        desc.setStyleSheet("font-size: 14px; color: #6c757d;")
        
        # Imagem da águia
        eagle_container = QWidget()
        eagle_layout = QVBoxLayout()
        eagle_layout.setAlignment(Qt.AlignCenter)
        
        try:
            response = requests.get("https://images.vexels.com/media/users/3/276346/isolated/lists/7fa6f3da3f76ce93766da46fc8667df7-elemento-desenhado-a-mao-de-aguia-americana.png")
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            pixmap = pixmap.scaled(300, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            eagle_img = QLabel()
            eagle_img.setPixmap(pixmap)
            eagle_img.setAlignment(Qt.AlignCenter)
            eagle_layout.addWidget(eagle_img)
        except:
            eagle_placeholder = QLabel("Imagem da Águia")
            eagle_placeholder.setAlignment(Qt.AlignCenter)
            eagle_placeholder.setStyleSheet("font-size: 14px; color: #6c757d; border: 1px dashed #ccc; padding: 40px;")
            eagle_layout.addWidget(eagle_placeholder)
        
        eagle_container.setLayout(eagle_layout)
        
        # Formulário de login
        form_layout = QVBoxLayout()
        form_layout.setSpacing(15)
        
        # Email
        email_label = QLabel("E-mail:")
        email_label.setStyleSheet("font-weight: bold;")
        email_input = QLineEdit()
        email_input.setPlaceholderText("seu@email.com")
        
        # Senha
        password_label = QLabel("Senha:")
        password_label.setStyleSheet("font-weight: bold;")
        password_input = QLineEdit()
        password_input.setPlaceholderText("Sua senha")
        password_input.setEchoMode(QLineEdit.Password)
        
        # Lembrar-me
        remember = QCheckBox("Lembrar-me")
        
        # Botão de login
        login_btn = QPushButton(" Entrar")
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: #2563eb; 
                color: white;
            }
            QPushButton:hover {
                background-color: #1e40af;
            }
            QPushButton:pressed {
                background-color: #1e3a8a;
            }
        """)
        login_btn.setIcon(self.get_icon("sign-in-alt"))
        login_btn.setIconSize(QSize(20, 20))
        login_btn.clicked.connect(self.do_login)
        
        # Esqueci a senha
        forgot = QLabel('<a href="#" style="color: #2563eb; text-decoration: none;">Esqueci minha senha</a>')
        forgot.setAlignment(Qt.AlignCenter)
        forgot.setOpenExternalLinks(False)
        forgot.linkActivated.connect(self.forgot_password)
        
        # Adicionando ao formulário
        form_layout.addWidget(email_label)
        form_layout.addWidget(email_input)
        form_layout.addWidget(password_label)
        form_layout.addWidget(password_input)
        form_layout.addWidget(remember)
        form_layout.addWidget(login_btn)
        form_layout.addWidget(forgot)
        
        # Seção de funcionalidades
        features = QFrame()
        features.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        features_layout = QVBoxLayout()
        
        features_title = QLabel("Funcionalidades do Sistema")
        features_title.setAlignment(Qt.AlignCenter)
        features_title.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 15px;")
        
        # Grid de funcionalidades
        features_grid = QHBoxLayout()
        
        # Funcionalidade 1
        feat1 = QVBoxLayout()
        feat1.setAlignment(Qt.AlignCenter)
        icon1 = self.create_icon("users", "#2563eb")
        title1 = QLabel("Controle de Atendimentos")
        title1.setAlignment(Qt.AlignCenter)
        title1.setStyleSheet("font-weight: bold;")
        desc1 = QLabel("Registro de famílias, jovens e crianças")
        desc1.setAlignment(Qt.AlignCenter)
        desc1.setStyleSheet("font-size: 12px; color: #6c757d;")
        
        feat1.addWidget(icon1)
        feat1.addWidget(title1)
        feat1.addWidget(desc1)
        
        # Funcionalidade 2
        feat2 = QVBoxLayout()
        feat2.setAlignment(Qt.AlignCenter)
        icon2 = self.create_icon("chart-line", "#2563eb")
        title2 = QLabel("Relatórios e Estatísticas")
        title2.setAlignment(Qt.AlignCenter)
        title2.setStyleSheet("font-weight: bold;")
        desc2 = QLabel("Geração de relatórios para análise")
        desc2.setAlignment(Qt.AlignCenter)
        desc2.setStyleSheet("font-size: 12px; color: #6c757d;")
        
        feat2.addWidget(icon2)
        feat2.addWidget(title2)
        feat2.addWidget(desc2)
        
        features_grid.addLayout(feat1)
        features_grid.addLayout(feat2)
        
        features_layout.addWidget(features_title)
        features_layout.addLayout(features_grid)
        features.setLayout(features_layout)
        
        # Adicionando tudo ao corpo
        body_layout.addWidget(welcome)
        body_layout.addWidget(desc)
        body_layout.addWidget(eagle_container)
        body_layout.addLayout(form_layout)
        body_layout.addWidget(features)
        
        body.setLayout(body_layout)
        
        # Rodapé
        footer = QLabel("ONG Mãe Águia © 2025 - Todos os direitos reservados")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: white; font-size: 12px; padding: 10px; background-color: #1e40af;")
        footer.setFixedHeight(40)
        
        # Adicionando ao layout principal
        main_layout.addWidget(header)
        main_layout.addWidget(body)
        main_layout.addWidget(footer)
        
        self.setLayout(main_layout)
        
        # Armazenar referências para os campos
        self.email_input = email_input
        self.password_input = password_input
        
    def create_icon(self, name, color):
        # Esta é uma implementação simplificada - em produção, você usaria ícones reais
        icon = QLabel()
        icon.setAlignment(Qt.AlignCenter)
        icon.setStyleSheet(f"font-size: 32px; color: {color}; font-weight: bold;")
        icon.setText("●")  # Placeholder para ícone
        icon.setFixedSize(40, 40)
        return icon
        
    def get_icon(self, name):
        # Esta função retornaria um QIcon real baseado no nome
        # Por simplicidade, estamos retornando um ícone vazio
        from PyQt5.QtGui import QIcon
        return QIcon()
        
    def do_login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        
        if email and password:
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.information(self, "Sucesso", "Login realizado com sucesso! Redirecionando...")
        else:
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Atenção", "Por favor, preencha todos os campos.")
            
    def forgot_password(self):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(self, "Recuperar Senha", "Funcionalidade de recuperação de senha em desenvolvimento.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Definindo a paleta de cores para o aplicativo
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(37, 99, 235))
    app.setPalette(palette)
    
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())