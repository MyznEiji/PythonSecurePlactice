

# Requirement

- Python3
- KaliLinux
- WordPress


# Usage

1. $ apachectl start
2. $ ifconfig -a
3. URL = IP Address 
4. mkdir /var/www/html/blog
5. Link copy WordPress : https://ja.wordpress.org/download/
6. $ wget https://ja.wordpress.org/wordpress-4.9.6-ja.zip
7. $ unzip wordpress-4.7.3-ja.zip
8. $ mv /var/www/html/blog/wordpress/* ./
9. $ apt-get install mysql-server
10. $ apt-get install mariadb-server
11. $ systemctl start mariadb
12. $ mysql_secure_installation
  - Y
  - Password
  - Y 
  - Y
  - Y
  - Y
13. $ mysql -u root -p
    - > create database wordpress;
    - > grant all on wordpress.* to bloguser@localhost identified by 'p@ssw0rd';
    - > flush pricileges;
    - > exit();
14. URL = IP Address/blog
15. touch /var/www/html/blog/wp-config.php 


# INFO
UserName : bloguser
PassWord : p@ssw0rd
