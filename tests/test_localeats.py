
from playwright.sync_api import sync_playwright


# Responsável: Matheus Souza dos Santos
def test_exibicao_formulario_cadastro():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=True)
        pagina = navegador.new_page()

        pagina.goto(
            "https://local-eats-unisenac.vercel.app/static/index.html"
        )

        # Interação: acessar a tela de cadastro
        pagina.get_by_text("Criar Conta").click()

        # Verificar os campos do formulário
        assert pagina.locator("#regName").is_visible()
        assert pagina.locator("#regEmail").is_visible()

        # Verificar o botão de registro
        assert pagina.get_by_role(
            "button", name="Registrar"
        ).is_visible()

        navegador.close()
