from Products.CMFCore.utils import getToolByNamedef install(self):    mdtool = getToolByName(self, 'portal_memberdata')    if not mdtool.hasProperty('ploneradio_role'):        mdtool._setProperty('ploneradio_role', 'Member', 'string')