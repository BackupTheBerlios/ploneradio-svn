#------------------------------------------------------------------------------# Name:         Teamlisting.py# Purpose:      Displays all groups from site with all its members with icon, fullname, name and role ## Author:       Wolfgang Reutz <wolfgang.reutz@fh-vorarlberg.ac.at># generated by: ArchGenXML Version 1.0 http://sf.net/projects/archetypes/## Created:      Tue Apr  5 15:06:12 2005# RCS-ID:       $Id: Teamlisting.py,v 1.1 2005/04/05 14:16:07 wreutz Exp $# Copyright:    (c) 2005 by Fachhochschule Vorarlberg# Licence:      GNU General Public Licence (GPL) Version 2 or later#------------------------------------------------------------------------------from AccessControl import ClassSecurityInfofrom Products.Archetypes.public import *    class Teamlisting(BaseContent):    '''    Displays all groups from site with all its members with icon, fullname, name and role    '''    security = ClassSecurityInfo()    portal_type = meta_type = 'Teamlisting'     archetype_name = 'Teamlisting'   #this name appears in the 'add' box     schema=BaseSchema  + Schema((        LinesField('ignore_groups',                    ),    ),    )    #Methods    # uncomment lines below when you need    factory_type_information={        'allowed_content_types':() ,        'content_icon':'ploneradio.gif',        'immediate_view':'base_view',        'global_allow':1,        'filter_content_types':1,        }            actions=  (                   {'action':      '''string:$object_url/teamlisting_view''',            'category':    '''object''',            'id':          'view',            'name':        'teamlisting_view',            'permissions': ('''View''',)},                    )        registerType(Teamlisting)# end of class Teamlisting