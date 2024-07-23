class DataReader:
    def readVerseInList(self, element: list, container: str, verseNo, flags):
        for a in range(len(element)):
            if element[a].id == "quote" or element[a].id == "seg" or element[a].id == "persName" or \
                    element[a].id == "said" or element[a].id == "l" or element[a].id == "lg" or element[a].id == "name":
                if element[a].id == "l":
                    if element[a].n == verseNo:
                        container = self._exploreVerse(element[a], container, flags)
                else:
                    if element[a].children:
                        container = self.readVerseInList(element[a].children, container, verseNo, flags)

        return container

    def read(self, element: list, container: str):
        for a in range(len(element)):
            if element[a].id == "quote" or element[a].id == "seg" or element[a].id == "persName" \
                    or element[a].id == "said" or element[a].id == "l" or element[a].id == "lg" \
                    or element[a].id == "name" or element[a].id == "add":
                container = self._explore(element[a], container)
            else:
                pass
                # print(element[a].id)
                # print("Unexpected Element occurred")
        return container

    def _explore(self, element, container: str):
        container += element.value

        if element.children:
            container = self.read(element.children, container)

        if element.tail is not None:
            container += element.tail

        return container

    def _exploreVerse(self, element, container: str, flags):
        if flags is None:
            container += element.value

            if element.children:
                container = self.read(element.children, container)
        elif flags == 'Tail':
            if element.tail is not None:
                container += element.tail

        return container
