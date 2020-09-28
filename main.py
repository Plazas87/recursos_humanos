import ezgmail


ezgmail.init()
for index, x in enumerate(ezgmail.unread()):
    var = index
    print(var)
    x.messages[0].downloadAllAttachments(downloadFolder='cv')

