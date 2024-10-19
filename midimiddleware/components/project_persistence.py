import json
import os.path

from midimiddleware.components.components import Components


class ProjectPersistence:

    def reset(self):
        Components().engine.stop()
        Components().port_selector.reset()
        Components().translator.reset()
        Components().engine.start()

    def open(self, filepath):
        Components().engine.stop()

        if filepath is not None and os.path.exists(filepath):
            with open(filepath, "r") as file:
                data = json.load(file)

            version = data.get("file_version", 0)
            if version != 1:
                raise RuntimeError(f"The project file is in the wrong version: {version}, expected 1")

            Components().port_selector.init_with_saved_data(
                data["port_selector"]
            )
            Components().translator.init_with_saved_data(
                data["translations"]
            )

        Components().engine.start()

    def save(self, filepath):
        Components().engine.stop()

        data = {
            "file_version": 1,
            "port_selector": Components().port_selector.get_save_data(),
            "translations": Components().translator.get_save_data()
        }
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

        Components().engine.start()
