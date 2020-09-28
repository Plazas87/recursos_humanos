import ezgmail


ezgmail.init()
for index, x in enumerate(ezgmail.unread()):
    var = index
    x.messages[0].downloadAllAttachments(downloadFolder='cv')

