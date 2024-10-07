import json

from midimiddleware.components.components import Components


class ProjectPersistence:

    def open(self, filepath):
        Components().engine.stop()

        with open(filepath, "r") as file:
            data = json.load(file)

        Components().port_selector.init_with_saved_data(
            data["port_selector"]
        )

        Components().engine.start()

    def save(self, filepath):
        Components().engine.stop()

        data = {
            "port_selector": Components().port_selector.get_save_data()
        }
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

        Components().engine.start()
