#create a new vm
from createVMClass import Provision
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import greenlet
import testdata1

try:
    A = Provision()
    A.getweb(testdata1.windows_username, testdata1.windows_password, testdata1.website)
    n = 0
    Domain_Region_List = A.get_domain_region(testdata1.domains, testdata1.regions)
    print Domain_Region_List
    for itemDRL in Domain_Region_List:
        for itemos in testdata1.os_flavor:
            A.get_datacenter_list(itemDRL[0], itemDRL[1])
            print itemDRL
            A.driver.find_element_by_xpath(testdata1.os_flavor[itemos]).click()
            A.get_diff_vlan(itemDRL[2], itemDRL[3])
            sleep(2)
            print "Domain, Region, Datacenter, OS type have been selected"
            if itemDRL[2] == 'ORG' and itemos in ('Windows 7',
                                                    'Windows Server 2008',
                                                    'Windows Server 2008 R2',
                                                    'Windows Server 2012',
                                                    'Windows Server 2012 R2'):
                A.get_windows_update()
                print "Windows update option has been selected"
            A.get_envinfo()
            #A.driver.find_element_by_xpath('//*[@id="form-field-vm-sizing"]').click()
            #A.driver.find_element_by_partial_link_text(testdata1.vm_size[0])
            A.get_extra_disk(testdata1.extra_disk_size_1, testdata1.extra_disk_size_2,
                             testdata1.extra_disk_size_3, testdata1.extra_disk_size_4,
                             testdata1.extra_disk_size_5)
            print "Tag, Extra_Disk have been set"
            n += 1
            m = str(n)
            A.driver.find_element_by_xpath('//*[@id="form-field-vm-name"]').send_keys(testdata1.vm_name + m)
            sleep(5)
            A.driver.refresh()
            sleep(5)



    #print Domain_Region_List
finally:
    sleep(10)
    A.logout()

