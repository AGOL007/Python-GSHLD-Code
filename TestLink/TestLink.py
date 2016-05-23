
import xmlrpclib


class TestlinkAPIClient:
    # substitute your server URL Here
    SERVER_URL = "http://172.16.1.151:8083/testlink/index.php?caller=login"

    def __init__(self, devKey):
        self.server = xmlrpclib.Server(self.SERVER_URL)
        self.devKey = devKey
        print "devKey in init: %s" %devKey

    def getTestCaseIDByName(self,devKey):
        data = {"devKey":devKey, "testcasename":"Test Case 1", "testsuitename":"Test Suite 1"}
        return self.server.tl.getTestCaseIDByName(data)

    def reportTCResult(self, tcid, tpid, status):
        data = {"devKey":self.devKey, "tcid":tcid, "tpid":tpid, "status":status}
        return self.server.tl.reportTCResult(data)

    def getInfo(self):
        return self.server.tl.about()

    def sayHello (self):
        return self.server.tl.sayHello()

    def getProjects (self, devKey):
        print "DevKey: %s" %devKey
        data = {"devKey":devKey}
        return self.server.tl.getProjects(data)

if __name__ == '__main__':
    devKey = "d5e563245413a9f2d2a0bc98d40ec264"
    # substitute your Dev Key Here
    client = TestlinkAPIClient (devKey)
    # get info about the server
    print client.getInfo()

    # retval = client.sayHello()

    #retval = client.getProjects(devKey)
    retval = client.getTestCaseIDByName(devKey)

    print 'retval: ', retval






