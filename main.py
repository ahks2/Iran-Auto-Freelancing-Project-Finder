import ui
import ponisha_scraper
import karlancer_scraper
import open_urls


DRIVER_PATH = r"C:\Users\User\Downloads\Compressed\geckodriver.exe"


def main():

    ui_instance = ui.UI()

    field, search, price = ui_instance.start()

    if price == 0:
        return

    print("Starting Ponisha scraper...")

    ponisha_scraper.run_ponisha_scraper(DRIVER_PATH,price)

    print("Ponisha finished")
    print("Starting Karlancer scraper...")

    karlancer_scraper.run_karlancer_scraper(DRIVER_PATH,price)

    print("Karlancer finished")
    print("Opening pages in browser")

    open_urls.open_urls()

    print("All tasks completed.")

if __name__ == "__main__":
    main()
