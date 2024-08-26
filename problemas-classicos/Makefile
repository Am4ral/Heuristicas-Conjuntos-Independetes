# Variáveis
VENV_DIR = src/.venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

# Alvo principal
all: run

# Cria o ambiente virtual
$(VENV_DIR):
	@echo "Criando o ambiente virtual..."
	python3 -m venv $(VENV_DIR)

# Instala as dependências
install: $(VENV_DIR)
	@echo "Instalando dependências..."
	$(PIP) install -r src/requirements.txt

# Executa o main.py
run: install
	@echo "Executando o main.py..."
	$(PYTHON) src/main.py

# Limpa o ambiente virtual
clean:
	@echo "Removendo o ambiente virtual..."
	rm -rf $(VENV_DIR)

.PHONY: all install run clean
