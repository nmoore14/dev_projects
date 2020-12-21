<?php
/**
 * This is to over ride or add to existing WordPress functions
 * 
 * PHP Version 7.23
 * 
 * @category WP_Functions
 * @package  WP_Theming_Blog
 * @author   Nick Moore <nickmoore_1@live.com>
 * @license  PHP License 3.01
 * @link     https://github.com/nmoore14
 */

/**
 * Functions to add theme info support
 * 
 * @return no return value
 */
function Nick_One_Theme_support()
{
    add_theme_support('title-tag');
}

add_action('after_theme_setup', 'Nick_One_Theme_support');

/**
 * Functions to add content to wp_enqueue_styles hook
 * 
 * @return no return value
 */
function Nick_One_Register_styles() 
{
    /**
     * Adds links to custom css styles to head
     */
    $version = wp_get_theme()->get( 'Version' );

    wp_enqueue_style(
        'nick-template-style',
        get_template_directory_uri() . '/style.css', 
        array('bootstrap'),
        $version,
        'all'
    );
    wp_enqueue_style(
        'bootstrap',
        'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css',
        array(),
        '5.0.0-beta1',
        'all'
    );
}

add_action('wp_enqueue_scripts', 'Nick_One_Register_styles');

/**
 * Functions to add content to wp_enqueue_scripts hook
 * 
 * @return no return value
 */
function Nick_One_Register_scripts()
{
    /**
     * Adds links to custom js
     */

    wp_enqueue_script(
        'bootstrap-js',
        'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js',
        array(),
        '5.0.0-beta1',
        true
    );
    wp_enqueue_script(
        'nick-template-script',
        get_template_directory_uri() . '/assets/js/main.js',
        array(),
        '1.0.0',
        true
    );
}

add_action('wp_enqueue_scripts', 'Nick_One_Register_scripts');

?>
