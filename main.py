import ui
import ponisha_scraper
import karlancer_scraper


DRIVER_PATH = r"YOUR GEKO DRIVER LOCATION"


def main():

    ui_instance = ui.UI()

    field, search, price = ui_instance.start()

    if price == 0:
        return

    print("Starting Ponisha scraper...")

    ponisha_scraper.run_ponisha_scraper(
        DRIVER_PATH,
        price
    )

    print("Ponisha finished")

    print("Starting Karlancer scraper...")

    karlancer_scraper.run_karlancer_scraper(
        DRIVER_PATH,
        price
    )

    print("Karlancer finished")
    print("All tasks done")


if __name__ == "__main__":
    main()
