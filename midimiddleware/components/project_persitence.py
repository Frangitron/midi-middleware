import json
import os.path

from midimiddleware.components.components import Components


class ProjectPersistence:

    def reset(self):
        Components().port_selector.reset()

    def open(self, filepath):
        Components().engine.stop()

        if filepath is not None and os.path.exists(filepath):
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
