PloneRadio

  by Wolfgang Reutz <wolfgang.reutz@fh-vorarlberg.ac.at>

  developed at Vorarlberg University of Applied Sciences and is released under 
  the terms of GNU Public License Version 2 or higher.

  Please see http://gnu.org for more details.
  
  What is PloneRadio?

    PloneRadio is a Product for Zope/Plone featuring tools to build a webbased
    radiostation with Plone. It provides a portlet to display up to 2 independent
    streams in two qualities and displays the album cover, title and artist of the
    currently playing track and with some servers it's possible to additioninally
    display the last few played tracks as well. Integrated in the portlet are
    different web players for quicktime, windowsmedia and a embedded java player.
    
    It includes tools to build a portal for a StreamOnTheFly node for displaying
    archived radio shows directly from the node using plone as frontend.

    It's aimed at community radio and free radio stations or bands providing
    livestreams on their plone based band homepage.
    
  Dependencies

    o PloneRadio is built using Archetypes 1.3.1-final and therefore depends on it.

    o you will need a mp3 streaming server (Icecast2, Icecast 1.x, QTSS, DSS will do)

    o a mp3 streaming source is also needed to send the stream to the server
      (Nicecast, icegenerator, liveice, ...)

    o mp3's to stream :-) please consider to use open content or your own material

  Installation
  
    Install in the usual way, using the QuickInstaller.
    
    Tested with Plone 2.0.5 and Archetypes 1.3.1-final.

  Configuration

    Configuration is done in the PloneRadio Preferences configlet in the plone setup
    page of your plone instance (need to be logged in with manager privileges). Enter
    the urls to your streams according to your server structure and setup.

    If you consider to use Nicecast to stream your broadcasts just fire it up and use
    the builtin icecast 1.x server. Then choose "nicecast" for the logfile type and
    choose wether you like to show recently played song and so on.

    If you use an Icecast2 server, you have to copy the file "ploneradio_current.xsl"
    from the doc/icecast2/ directory of this product to the web folder of your icecast2
    server (something like /usr/local/icecast2/share/icecast/web/). If you have problems
    to find the right directory, search for "status2.xsl" as this file should be in this
    directory. Then choose "icecast" for the logfile type. For icecast2 there is no
    display of recently played songs yet but you can choose if you want to show the number
    of current listeners.

    To add the portlet to your page, go to the ZMI and add the following line to the 
    left_slots or right_slots section in the properties of your plone site:
    here/portlet_ploneradio/macros/portlet
    
  Documentation

    For full documentation go to http://option.uclv.net/rw/streaming/ploneradio/

  Bugs

    Please report bugs to wolfgang.reutz@fh-vorarlberg.ac.at

  Modification
  
    PloneRadio was created using ArchGenXML. The UML model is in the model/
    directory. The .odm file is the original model created using ObjectDomain 
    version 3. The .xmi file is the XMI file read by ArchGenXML.
    
  Known Issues and Potential Improvements
  
    o Non-standard characters from Nicecast and Icecast2 logfiles are not handled
      correctly.

    o flash player with display of the title / artist for maximum user experience.

    o analysis of the playlist history

    o voting system for the playlist / user requests
    
    o interface for dj's to build playlist for their broadcasts online and a scheduler for playing the different shows(playlists) automatically

    o in sotf listings (station/series/queries) add function to select streams/files and get a m3u for listening to them as a stream
    
  To Do

    o java player
    
    o windows media player not working with mozilla browsers on mac/pc
    
    o sotf rss 2.0 output needed for series, programme, query
    
    o sotf rss 2.0 namespace enhaced for series, programme, query
    
    o maybe feedparser needs modification for series, programme, query
    
    o page template for viewing of programme from the station/series/query listing, maybe a document type for a single programme
    
    o document type for series
    
    o document type for query
    
    o documentation about rss 2.0 bridge SOTF on http://sotf.sourceforge.net/rss/2.0/modules/sotf
    

  