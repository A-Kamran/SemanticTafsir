class div:
    def __init__(self):
        self.id = "div"
        self.type = None
        self.n = None
        self.value = ''
        self.language = None
        self.children = []
        self.tail = None


class head:
    def __init__(self):
        self.id = "head"
        self.type = None
        self.n = None
        self.value = ''
        self.children = []
        self.tail = None


class p:
    def __init__(self):
        self.id = "p"
        self.n = None
        self.p_id = None
        self.ana = None
        self.value = ''
        self.children = []
        self.tail = None


class quote:
    def __init__(self):
        self.id = "quote"
        self.type = None
        self.n = None
        self.q_id = None
        self.value = ''
        self.subType = ''
        self.children = []
        self.tail = None


class seg:
    def __init__(self):
        self.id = "seg"
        self.ana = None
        self.value = ''
        self.children = []
        self.tail = None


class lb:
    def __init__(self):
        self.id = "lb"
        self.n = None
        self.value = ''
        self.children = []
        self.tail = None


class note:
    def __init__(self):
        self.id = "note"
        self.value = ''
        self.children = []
        self.tail = None


class persName:
    def __init__(self):
        self.id = "persName"
        self.ana = None
        self.value = ''
        self.type = ''
        self.n = None
        self.children = []
        self.tail = None


class said:
    def __init__(self):
        self.id = "said"
        self.value = ''
        self.s_id = None
        self.children = []
        self.tail = None


class pb:
    def __init__(self):
        self.id = 'pb'
        self.ed = None
        self.edRef = None
        self.n = None
        self.ed = None
        self.type = None
        self.children = []
        self.tail = None


class l:
    def __init__(self):
        self.id = 'l'
        self.value = ''
        self.n = None
        self.children = []
        self.tail = None


class lg:
    def __init__(self):
        self.id = 'lg'
        self.children = []
        self.tail = None


class name:
    def __init__(self):
        self.id = "name"
        self.value = ''
        self.type = ''
        self.role = None
        self.tail = None
        self.children = []


class add:
    def __init__(self):
        self.id = "add"
        self.value = ''
        self.type = ''
        self.tail = None
        self.children = []
