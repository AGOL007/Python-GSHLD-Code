

from Testlink.testlink import TestlinkAPIClient

dev_key = "d5e563245413a9f2d2a0bc98d40ec264"
server_url = "http://172.16.1.151:8083/testlink/index.php?caller=login"

if __name__ == "__main__":
    client = TestlinkAPIClient(dev_key, server_url)
    client.getTestCase(2)
# Substitute for tcid and tpid that apply to your project
    if 0:
        result = client.reportTCResult(103, 109, "p")
    else:
        result = client.reportTCResult(103, 109, "f")
# Typically you'd want to validate the result here and probably do something more useful with it
    print "reportTCResult result was: %s" %(result)
