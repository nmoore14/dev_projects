<?php
function nickone_register_styles() {
  wp_enqueue_style('nick-template-style', get_template_directory_uri() . '/style.css', array(), '1.0', 'all');
}

add_action('wp_enqueue_scripts', 'nickone_register_styles');

?>
