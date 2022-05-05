<!DOCTYPE html>
<!-- saved from url=(0030)http://localhost:5000/login -->
<html class="fontawesome-i2svg-active fontawesome-i2svg-complete">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <meta content="width=device-width, initial-scale=1" name="viewport">
    <!--<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.0/css/bulma.min.css">-->

    <link href="./Ruby_files/bulma.min.css" rel="stylesheet">
    <link href="./Ruby_files/site.css" rel="stylesheet">
    <!--<script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>-->
    <script defer="" src="./Ruby_files/fa.js"></script>
    <!--<script src="https://cdn.jsdelivr.net/npm/@vizuaalog/bulmajs@0.10.2/dist/bulma.js"></script>-->
    <script src="./Ruby_files/bulma.js"></script>
    <title>WELCOME</title>
</head>

<body>
    <section class="section">
        <div class="container">
            <h1 class="title">
                Weclome to XiaBee's Website!
            </h1>
            <div class="notification is-primary hidden" data-bulma-attached="attached">
                <button class="delete"></button>
            </div>
            <div class="tabs-wrapper" data-bulma-attached="attached">
                <div class="tabs">
                    <ul>
                        <li class="is-active">
                            <a>Login</a>
                        </li>
                        <li class="">
                            <a>Register</a>
                        </li>
                    </ul>
                </div>
                <div class="tabs-content">
                    <ul>
                        <li class="is-active">
                            <form action="http://localhost:5000/index.php" method="GET" _lpchecked="1">
                                <div class="field">
                                    <label class="label">ID</label>
                                    <div class="control has-icons-left">
                                        <input class="input" name="id" placeholder="demo" type="text" autocomplete="off">
                                    </div>
                                </div>
                                <div class="control">
                                    <button class="button is-primary" type="submit">Query</button>
                                    <?php
                                        include "./config.php";
                                        // error_reporting(-1);
                                        // highlight_file(__FILE__);

                                        $conn = mysqli_connect($hostname, $username, $password, $database);
                                        if ($conn->connect_errno) {
                                            die("Connection failed: " . $conn->connect_errno);
                                            # php版本升级，报错处理暂时没有处理好
                                        } 

                                        if (isset($_GET['id'])) {
                                            $id = $_GET['id'];
                                            $sql = "select * from users where id=$id";
                                            $result = mysqli_query($conn, $sql);
                                            if ($result) {
                                                $row = mysqli_fetch_array($result);
                                                echo "<h3>" . $row['username'] . "</h3><br>";
                                                echo "<h3>" . $row['passwd'] . "</h3>";
                                            }
                                            else {
                                                die('<br>.Could not connect: '.mysqli_errno($conn));
                                                # php版本升级，报错处理暂时没有处理好
                                            }
                                        }
                                        mysqli_close($con); 
                                        ?>
                                </div>
                            </form>
                        </li>
                        <li class="">
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="content has-text-centered">

        </div>
    </footer>

</body>

</html>