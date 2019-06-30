var ypos,id;
function parallex(){
	ypos= window.pageYOffset;
	id= document.document.getElementById('img');
	id.style.top=ypos*1+'px';

	
}
window.addEventListener('scroll',parallex);
