import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QCheckBox, QFrame,
                             QSizePolicy, QMessageBox)
from PyQt5.QtGui import QPixmap, QFont, QPalette, QColor
from PyQt5.QtCore import Qt

class FullScreenLoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mãe Águia - Sistema de Controle de Atendimentos")
        
        # Inicializar atributos para evitar AttributeError
        self.email_input = None
        self.password_input = None
        
        # Configurar para modo tela cheia
        self.showMaximized()
        
        # Configurar a paleta de cores
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(37, 99, 235))
        self.setPalette(palette)
        
        self.initUI()
        
    def initUI(self):
        # Layout principal com margens para criar borda
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setContentsMargins(50, 50, 50, 50)  # Borda ao redor do conteúdo
        
        # Container central com borda arredondada
        central_container = QFrame()
        central_container.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;
                border: 2px solid #1e3a8a;
            }
        """)
        central_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        central_container.setMaximumWidth(1000)  # Largura máxima do conteúdo
        central_container.setMaximumHeight(800)  # Altura máxima do conteúdo
        
        central_layout = QVBoxLayout()
        central_layout.setAlignment(Qt.AlignCenter)
        central_layout.setSpacing(0)
        central_layout.setContentsMargins(0, 0, 0, 0)
        
        # Cabeçalho
        header = QFrame()
        header.setFixedHeight(150)
        header.setStyleSheet("""
            QFrame {
                background-color: #1e40af; 
                border-top-left-radius: 18px;
                border-top-right-radius: 18px;
            }
        """)
        header_layout = QVBoxLayout()
        header_layout.setAlignment(Qt.AlignCenter)
        
        title = QLabel("Associação Mãe Águia")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: white;")
        
        subtitle = QLabel("Sistema de Controle de Atendimentos")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 18px; color: white;")
        
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        header.setLayout(header_layout)
        
        # Corpo do login
        body = QFrame()
        body.setStyleSheet("""
            QFrame {
                background-color: white;
                border-bottom-left-radius: 18px;
                border-bottom-right-radius: 18px;
            }
        """)
        body_layout = QVBoxLayout()
        body_layout.setAlignment(Qt.AlignCenter)
        body_layout.setSpacing(25)
        body_layout.setContentsMargins(40, 40, 40, 40)
        
        # Título de boas-vindas
        welcome = QLabel("Bem-vindo, colaborador!")
        welcome.setAlignment(Qt.AlignCenter)
        welcome.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        desc = QLabel("Aqui você trabalha em pró da família")
        desc.setAlignment(Qt.AlignCenter)
        desc.setStyleSheet("font-size: 16px; color: #6c757d;")
        
        # Imagem da águia
        eagle_container = QWidget()
        eagle_layout = QVBoxLayout()
        eagle_layout.setAlignment(Qt.AlignCenter)
        
        try:
            response = requests.get(
                "https://images.vexels.com/media/users/3/276346/isolated/lists/7fa6f3da3f76ce93766da46fc8667df7-elemento-desenhado-a-mao-de-aguia-americana.png",
                timeout=10
            )
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            pixmap = pixmap.scaled(350, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            eagle_img = QLabel()
            eagle_img.setPixmap(pixmap)
            eagle_img.setAlignment(Qt.AlignCenter)
            eagle_layout.addWidget(eagle_img)
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            eagle_placeholder = QLabel("Imagem da Águia")
            eagle_placeholder.setAlignment(Qt.AlignCenter)
            eagle_placeholder.setStyleSheet("""
                font-size: 16px; 
                color: #6c757d; 
                border: 2px dashed #ccc; 
                padding: 60px; 
                border-radius: 10px;
            """)
            eagle_layout.addWidget(eagle_placeholder)
        
        eagle_container.setLayout(eagle_layout)
        
        # Formulário de login
        form_container = QWidget()
        form_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        form_layout = QVBoxLayout()
        form_layout.setAlignment(Qt.AlignCenter)
        form_layout.setSpacing(20)
        
        # Email
        email_container = QWidget()
        email_container_layout = QVBoxLayout()
        email_container_layout.setAlignment(Qt.AlignCenter)
        email_label = QLabel("E-mail:")
        email_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        email_label.setAlignment(Qt.AlignCenter)
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("seu@email.com")
        self.email_input.setMinimumWidth(300)
        self.email_input.setMaximumWidth(400)
        self.email_input.setStyleSheet("font-size: 16px; padding: 12px;")
        email_container_layout.addWidget(email_label)
        email_container_layout.addWidget(self.email_input)
        email_container.setLayout(email_container_layout)
        
        # Senha
        password_container = QWidget()
        password_container_layout = QVBoxLayout()
        password_container_layout.setAlignment(Qt.AlignCenter)
        password_label = QLabel("Senha:")
        password_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        password_label.setAlignment(Qt.AlignCenter)
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Sua senha")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumWidth(300)
        self.password_input.setMaximumWidth(400)
        self.password_input.setStyleSheet("font-size: 16px; padding: 12px;")
        password_container_layout.addWidget(password_label)
        password_container_layout.addWidget(self.password_input)
        password_container.setLayout(password_container_layout)
        
        # Lembrar-me
        remember_container = QWidget()
        remember_container_layout = QHBoxLayout()
        remember_container_layout.setAlignment(Qt.AlignCenter)
        self.remember = QCheckBox("Lembrar-me")
        self.remember.setStyleSheet("font-size: 14px;")
        remember_container_layout.addWidget(self.remember)
        remember_container.setLayout(remember_container_layout)
        
        # Botão de login
        login_container = QWidget()
        login_container_layout = QHBoxLayout()
        login_container_layout.setAlignment(Qt.AlignCenter)
        login_btn = QPushButton(" Entrar")
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: #2563eb; 
                color: white;
                padding: 15px;
                border-radius: 10px;
                font-size: 18px;
                min-width: 250px;
            }
            QPushButton:hover {
                background-color: #1e40af;
            }
            QPushButton:pressed {
                background-color: #1e3a8a;
            }
        """)
        login_btn.clicked.connect(self.do_login)
        login_container_layout.addWidget(login_btn)
        login_container.setLayout(login_container_layout)
        
        # Esqueci a senha
        forgot_container = QWidget()
        forgot_container_layout = QHBoxLayout()
        forgot_container_layout.setAlignment(Qt.AlignCenter)
        forgot = QLabel('<a href="#" style="color: #2563eb; text-decoration: none; font-size: 14px;">Esqueci minha senha</a>')
        forgot.setOpenExternalLinks(False)
        forgot.linkActivated.connect(self.forgot_password)
        forgot_container_layout.addWidget(forgot)
        forgot_container.setLayout(forgot_container_layout)
        
        # Adicionando ao formulário
        form_layout.addWidget(email_container)
        form_layout.addWidget(password_container)
        form_layout.addWidget(remember_container)
        form_layout.addWidget(login_container)
        form_layout.addWidget(forgot_container)
        form_container.setLayout(form_layout)
        
        # Seção de funcionalidades
        features = QFrame()
        features.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border-radius: 15px;
                padding: 25px;
                border: 1px solid #e9ecef;
            }
        """)
        features_layout = QVBoxLayout()
        features_layout.setAlignment(Qt.AlignCenter)
        
        features_title = QLabel("Funcionalidades do Sistema")
        features_title.setAlignment(Qt.AlignCenter)
        features_title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px;")
        
        # Grid de funcionalidades
        features_grid = QHBoxLayout()
        features_grid.setAlignment(Qt.AlignCenter)
        features_grid.setSpacing(40)
        
        # Funcionalidade 1
        feat1_container = QWidget()
        feat1 = QVBoxLayout()
        feat1.setAlignment(Qt.AlignCenter)
        feat1.setSpacing(10)
        icon1 = QLabel("👥")
        icon1.setAlignment(Qt.AlignCenter)
        icon1.setStyleSheet("font-size: 40px;")
        title1 = QLabel("Controle de Atendimentos")
        title1.setAlignment(Qt.AlignCenter)
        title1.setStyleSheet("font-size: 16px; font-weight: bold;")
        desc1 = QLabel("Registro de famílias, jovens e crianças")
        desc1.setAlignment(Qt.AlignCenter)
        desc1.setStyleSheet("font-size: 14px; color: #6c757d;")
        
        feat1.addWidget(icon1)
        feat1.addWidget(title1)
        feat1.addWidget(desc1)
        feat1_container.setLayout(feat1)
        
        # Funcionalidade 2
        feat2_container = QWidget()
        feat2 = QVBoxLayout()
        feat2.setAlignment(Qt.AlignCenter)
        feat2.setSpacing(10)
        icon2 = QLabel("📊")
        icon2.setAlignment(Qt.AlignCenter)
        icon2.setStyleSheet("font-size: 40px;")
        title2 = QLabel("Relatórios e Estatísticas")
        title2.setAlignment(Qt.AlignCenter)
        title2.setStyleSheet("font-size: 16px; font-weight: bold;")
        desc2 = QLabel("Geração de relatórios para análise")
        desc2.setAlignment(Qt.AlignCenter)
        desc2.setStyleSheet("font-size: 14px; color: #6c757d;")
        
        feat2.addWidget(icon2)
        feat2.addWidget(title2)
        feat2.addWidget(desc2)
        feat2_container.setLayout(feat2)
        
        features_grid.addWidget(feat1_container)
        features_grid.addWidget(feat2_container)
        
        features_layout.addWidget(features_title)
        features_layout.addLayout(features_grid)
        features.setLayout(features_layout)
        
        # Adicionando tudo ao corpo
        body_layout.addWidget(welcome)
        body_layout.addWidget(desc)
        body_layout.addWidget(eagle_container)
        body_layout.addWidget(form_container)
        body_layout.addWidget(features)
        
        body.setLayout(body_layout)
        
        # Adicionando cabeçalho e corpo ao container central
        central_layout.addWidget(header)
        central_layout.addWidget(body)
        central_container.setLayout(central_layout)
        
        # Adicionando o container central ao layout principal
        main_layout.addWidget(central_container)
        
        # Rodapé - sempre centralizado na parte inferior
        footer = QLabel("ONG Mãe Águia © 2025 - Todos os direitos reservados")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: white; font-size: 14px; padding: 15px;")
        footer.setFixedHeight(50)
        
        main_layout.addWidget(footer)
        
        self.setLayout(main_layout)
        
    def do_login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        
        if email and password:
            QMessageBox.information(self, "Sucesso", "Login realizado com sucesso! Redirecionando...")
        else:
            QMessageBox.warning(self, "Atenção", "Por favor, preencha todos os campos.")
            
    def forgot_password(self):
        QMessageBox.information(self, "Recuperar Senha", "Funcionalidade de recuperação de senha em desenvolvimento.")
        
    def resizeEvent(self, event):
        # Ajustar elementos com base no tamanho da janela
        super().resizeEvent(event)
        
        # Verificar se os campos já foram inicializados antes de acessá-los
        if self.email_input and self.password_input:
            width = self.width()
            max_field_width = min(400, width // 3)  # Ajusta com base na largura da tela
            
            self.email_input.setMaximumWidth(max_field_width)
            self.password_input.setMaximumWidth(max_field_width)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Definir a fonte padrão
    font = QFont("Arial", 12)
    app.setFont(font)
    
    window = FullScreenLoginWindow()
    window.show()
    sys.exit(app.exec_())