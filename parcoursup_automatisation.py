from settings import *

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://authentification.parcoursup.fr/Authentification/connexion")

email = driver.find_element(By.CLASS_NAME, "fr-input")
email.clear()
email.send_keys("USERNAME")

password = driver.find_element(By.CLASS_NAME, "fr-password__input")
password.clear()
password.send_keys("password")
password.send_keys(Keys.ENTER)

driver.get("https://dossier.parcoursup.fr/Candidat/authentification?redirect=compte")
time.sleep(1)
driver.execute_script("window.scrollTo(0, 1000)")
btn_afficher = driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/button")
btn_afficher.click()
time.sleep(1)

places = driver.find_elements(By.XPATH, "//*[@id='tableauxAdmissions_voeuxEnAttente_3']/ul/li/div/ul/li[2]/span[2]")
filieres = driver.find_elements(By.XPATH, "//*[@id='tableauxAdmissions_voeuxEnAttente_3']/ul/li/div[2]/div/div[1]/p[2]")
ecoles = driver.find_elements(By.XPATH, "//*[@id='tableauxAdmissions_voeuxEnAttente_3']/ul/li/div[2]/div/div[1]/p[1]")
messages = []

for i in range(len(ecoles)):
    message = f"->{places[i].text}ème pour {filieres[i].text}"
    messages.append(message)
    message_bis = f"au {ecoles[i].text}"
    messages.append(message_bis)
messages.append(" /!\ Message envoyé depuis un script python automatique /!\ ")

driver.quit()

#---------------------------------------------------------------------------------------

def draw_text(texte, font, couleur, x, y):
    img = font.render(texte, True, couleur)
    text_width, text_height = font.size(texte)
    SCREEN.blit(img, (x - text_width // 2, y - text_height // 2))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    CLOCK.tick(60)
    SCREEN.fill((87, 132, 186))
    draw_text("Files d'attente ParcourSup:", FONT_LILITAONE_50, CLR_WHITE, SCREEN_WIDTH // 2 - 30, 45)
    draw_text("© TraZe 2024", FONT_LILITAONE_10, CLR_WHITE, SCREEN_WIDTH - 30, SCREEN_HEIGHT - 5)

    for i in range(len(messages)):
        draw_text(f"{messages[i]}", FONT_LILITAONE_30, CLR_WHITE, SCREEN_WIDTH // 2, 95 + 50 * i + 30 * (i//2))

    pygame.display.update()

pygame.quit()