from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import Trello

edge_options = webdriver.EdgeOptions()
edge_options.add_argument("headless")
edge_options.add_argument("disable-gpu")

edge = webdriver.Edge("driver.exe", options=edge_options)
edge.get("https://alhassania.emadariss.net/Login?ReturnUrl=%2fEvents")

class App:
    def log_in(username="your_username", password="your_password"):
        user_field = edge.find_element(By.XPATH, "//input[@id='Username']")
        user_field.send_keys(username)

        pass_field = edge.find_element(By.XPATH, "//input[@id='Password']")
        pass_field.send_keys(password)

        log_in_btn = edge.find_element(By.XPATH, "//button[@type='submit']")
        log_in_btn.click()

    def get_events():
        events = edge.find_elements(By.CLASS_NAME, "fc-day-grid-event.fc-h-event.fc-event.fc-start.fc-end")
        titles = [title.text for title in events]
        data_ids = [data_id.get_attribute("data-id") for data_id in events if data_id.get_attribute("data-id") != None]

        for title in titles:
            edge.get(f"https://alhassania.emadariss.net/Events/EventShow/{data_ids[titles.index(title)]}")
            content = edge.find_element(By.XPATH, "//div[contains(@class,'modal-body')]").text

            if title in Trello.check_cards():
                pass
            else:
                Trello.send_card(name=title, desc=content)
if __name__ == "__main__":
    App.log_in()
    App.get_events()
