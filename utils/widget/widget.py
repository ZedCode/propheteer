import pyglet

# This file creates collections of widget objects and
# places them within the UI grid space and draws everything
# relative. Unlike menus, an arbitrary number of items can
# be tied together as a single UI object. Each element has
# it's own function bindings, so they are really related
# only by logical groupings.

class widgetUI(pyglet.sprite.Sprite):
    def __init__(self, widgetUp, widgetDown, clickable=False, *args, **kwargs):
        super(widgetUI, self).__init__(img=widgetUp, *args, **kwargs)
        self.widgetUp = widgetUp
        self.widgetDown = widgetDown
        self.clickable = clickable
    def checkPres(self, x, y):
        if not self.clickable:
            return False
        if (x > self.x - (self.width / 2) and x < self.x + (self.width / 2)) and \
        (y > self.y - (self.height / 2) and y < self.y + (self.height / 2)):
            self.downImage()
            return True
        else:
            return False
    def downImage(self):
        self.image = self.widgetDown
    def upImage(self):
        self.image = self.widgetUp

class widget():
    def __init__(self, x, y, widgetLayer, renderBatch):
        self.x = x
        self.y = y
        self.widgetLayer = widgetLayer
        self.renderBatch = renderBatch
        self.widgets = {}
    def add(self, name, widgetUp, widgetDown, xoffset, yoffset, action, clickable=clickable):
        uiObj = widgetUI(widgetUp=widgetUp,
                         widgetDown=widgetDown,
                         clickable=clickable,
                         x=self.x + xoffset,
                         y=self.y + yoffset)
        self.widgets[name] = [uiObj, action]
    def show(self):
        for k,v in self.widgets.iteritems():
            self.widgets[k][0].batch = self.renderBatch
    def hide(self):
        for k,v in self.widgets.iteritems():
            self.widgets[k][0].batch = None
    def destroy(self):
        # This cleans up all the object associations so
        # that this can be properly GC'd
        for k,v in self.widgets.iteritems():
            self.widgets[k][0].delete()
