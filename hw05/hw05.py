'''У вас есть список(list) IP адрессов. Вам необходимо создать
класс который сможет:
1) Получить и изменить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13)'''


class IpHandler:
    """Handles a list of IPs, each IP must be a string"""

    def __init__(self, ipList):
        self._ipList = ipList

    @property
    def ipList(self):
        return self._ipList

    @ipList.setter
    def ipList(self, newList):
        self.ipList = newList

    def reverse_IP(self):
        """Return it's IPs reversed"""
        return [self._reverse_single_ip(ip) for ip in self.ipList]

    def get_oct_1_3(self):
        """Returns a list of IPs without first octets (127.0.0.1 -> .0.0.1)"""
        return [self._get_single_oct_1_3(ip) for ip in self.ipList]

    def get_oct_3(self):
        """Returns a list of last octets of each IP (127.0.0.1 -> .1)"""
        return [self._get_single_oct_3(ip) for ip in self.ipList]

    def _reverse_single_ip(self, ip):
        reversed_ip = ip.split(".")
        reversed_ip.reverse()
        return ".".join(reversed_ip)

    def _get_single_oct_1_3(self, ip):
        return "." + ".".join(ip.split(".")[1:])

    def _get_single_oct_3(self, ip):
        return "." + ip.split(".")[3]


list_ip = ["111.22.33.44", "123.234.12.23", "127.0.0.1"]
handler = IpHandler(list_ip)
print(list_ip)
print(handler.reverse_IP())
print(handler.get_oct_1_3())
print(handler.get_oct_3())

'''Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и назначения этих атрибутов в классе.'''


class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, new_name):
        self._unit_name = new_name

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, new_mac):
        self._mac_address = new_mac

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def unit_name(self, new_ip):
        self._ip_address = new_ip

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login):
        self._login = new_login

    @property
    def password(self):
        return self._password

    @password.setter
    def unit_name(self, new_pass):
        self._password = new_pass
