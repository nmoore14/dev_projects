$(document).ready(function () {
	var isVisible = false;
	$("#search-icon").click(function () { 
		if(!isVisible) {
			$("#search-container").animate({
				opacity: '1',
				top: '0'
			})
			isVisible = true;
		} else {
			$("#search-container").animate({
				top: '-11.5rem',
				opacity: '0'
			})
			isVisible = false;
		}
	});
});