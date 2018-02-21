import pyglet

class buttonUI(pyglet.sprite.Sprite):
    def __init__(self, buttonUp, buttonDown, clickable=True, *args, **kwargs):
        super(buttonUI, self).__init__(img=buttonUp, *args, **kwargs)
        self.buttonUp = buttonUp
        self.buttonDown = buttonDown
        self.clickable = clickable
    def checkPress(self, x, y):
        # checks to see if a click happened within the bounds of this object
        # keep buttons square, otherwise this gets complex.
        if not self.clickable:
            return False
        if x > self.x - (self.width / 2) and x < self.x + (self.width / 2):
            if y > self.y - (self.height / 2) and y < self.y + (self.height / 2):
                self.downImage()
                return True
    def downImage(self):
        self.image = self.buttonDown
    def upImage(self):
        self.image = self.buttonUp

class menu():
    def __init__(self, x, y, buttonLayer, textLayer, renderBatch, buttonUp, buttonDown, horizontal=False, title=None):
        self.x = x
        self.y = y
        self.menuItems = {}
        self.labels = []
        self.readableLabels = []
        self.buttonLayer = buttonLayer
        self.renderBatch = renderBatch
        self.textLayer = textLayer
        self.buttonUp = buttonUp
        self.buttonDown = buttonDown
        self.horizontal = horizontal
        self.title = title
        self.titleObj = None
    def add(self, text, action):
        if self.horizontal:
            itemX = self.x + (self.buttonUp.width * len(self.menuItems))
            itemY = self.y
        else:
            itemX = self.x
            itemY = self.y - (self.buttonUp.height * len(self.menuItems))
        uiObj = buttonUI(x=itemX, y=itemY,
            batch=self.renderBatch,
            group=self.buttonLayer,
            buttonUp=self.buttonUp,
            buttonDown=self.buttonDown)
        self.menuItems[text] = [uiObj, action]

    def menuTitle(self):
        print("what")
        itemY = self.y + self.buttonUp.height
        if self.horizontal:
            itemX = self.x + (self.buttonUp.width / 2)
        else:
            itemX = self.x
        uiObj = buttonUI(x=itemX, y=itemY,
            batch=self.renderBatch,
            group=self.buttonLayer,
            buttonUp=self.buttonUp,
            buttonDown=self.buttonDown,
            clickable=False)
        self.titleObj = pyglet.text.HTMLLabel('<font face="Ariel" size="4">'+self.title+'</font>',
            x=itemX, y=itemY+3,
            anchor_x='center', anchor_y='center',
            batch=self.renderBatch, group=self.textLayer)

    def makeLabels(self):
        for k,v in self.menuItems.iteritems():
            self.labels.append(pyglet.text.HTMLLabel('<font face="Ariel" size="4">'+k+'</font>',
              x=v[0].x, y=v[0].y+3,
              anchor_x='center', anchor_y='center',
              batch=self.renderBatch, group=self.textLayer))
            self.readableLabels.append(k)
    def hide(self):
        for i in self.labels:
            i.batch = None
        for i in self.labels:
            i.delete()
        self.readableLabels = []
        for k,v in self.menuItems.iteritems():
            self.menuItems[k][0].batch = None
        if self.titleObj is not None:
            self.titleObj.batch = None
    def show(self):
        self.makeLabels()
        for k,v in self.menuItems.iteritems():
            self.menuItems[k][0].batch = self.renderBatch
        if self.titleObj is not None:
            self.titleObj.batch = self.renderBatch
