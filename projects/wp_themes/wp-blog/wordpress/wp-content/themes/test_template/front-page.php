<?php
// @codingStandardsIgnoreStart
?>

<?php
  get_header();
?>

<div class="container-fluid" id="main-content-container">
  <?php
    if(have_posts()) {
      while(have_posts()) {
        the_post();
        the_content();
      }
    }
  ?>
</div>

<?php
  get_footer();
?>
