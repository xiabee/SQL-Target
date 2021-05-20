# SQL-Target
* 基于布尔盲注与联合查询的`GETSHELL`渗透实战攻击



#### 项目结构

* 靶机：`./target`
* `POC`：`./poc`

```bash
.
├── poc
│   ├── README.md
│   ├── requirement.txt
│   └── sqli-getshell.py
├── README.md
└── target
    ├── docker-compose.yml
    ├── flag
    │   └── FLAG
    ├── mysql
    │   ├── init
    │   │   ├── privileges.sql
    │   │   └── schema.sql
    │   └── my.cnf
    ├── nginx
    │   └── nginx.conf
    ├── php
    │   ├── Dockerfile
    │   ├── php-fpm.conf
    │   └── php.ini
    ├── README.md
    └── www
        ├── config.php
        ├── FLAG
        ├── index.php
        └── Ruby_files
            ├── bulma.js
            ├── bulma.min.css
            ├── fa.js
            └── site.css

10 directories, 20 files
```

