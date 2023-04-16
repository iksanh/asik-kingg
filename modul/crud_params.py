#untuk parameter crud

class CrudParams:

    def __init__(self, modul):
        self._modul = modul.lower()

    @property
    def params(self):
        return {
            "modul": self._modul,
            "links": {
                "create": 'create-'+self._modul,
                "edit": 'edit-'+self._modul,
                "delete": 'delete-'+self._modul,
                "list": 'list-'+self._modul
            }
        }


# print(CrudParams('Pinjaman').params)