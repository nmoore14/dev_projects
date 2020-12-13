<?php
// @codingStandardsIgnoreStart
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <!-- PHP Head hook -->
        <?php
            wp_head();
        ?>
    </head>
    <body>
        <div class="container-fluid">
            <div class="row">
                <div class="col">
                    <h1><?php the_title(); ?></h1>
                </div>
            </div>
        </div>
