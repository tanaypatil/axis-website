// JavaScript Document

	var tag = document.createElement('script');
    tag.src = "http://www.youtube.com/player_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

    // 3. This function creates an <iframe> (and YouTube player)
    //    after the API code downloads.
    var player;
    function onYouTubePlayerAPIReady() {
        player = new YT.Player('player', {
            height: '395',
            width: '600',
            videoId: 'g6yGzaBVlz0',
        });
        document.getElementById('resume').onclick = function () {
            player.playVideo();
        };
        document.getElementById('pause').onclick = function () {
            player.pauseVideo();
        };
    }
	

		function change1(){
		var img,bckg,vid,iframe;
		img = document.getElementById("img");
		img.src= static_url +"/images/socini/colorsofngp.jpg";
		img.className="visible";
		bckg = document.getElementById("socini");
		bckg.style.background='url(images/socini/colorsofngp.jpg)';
		bckg.style.backgroundPosition="50% 50%";
		bckg.style.backgroundSize="cover";
		vid=document.getElementById("player");
		vid.className="hidden";
		iframe = document.getElementById("if");
		 player.pauseVideo();
		
	}
	
	function change2(){
		var img,bckg,vid;
		img = document.getElementById("img");
		img.src="images/socini/nosmoking.jpg";
		img.className="visible";
		bckg = document.getElementById("socini");
		bckg.style.background='url(images/socini/nosmoking.jpg)';
		bckg.style.backgroundPosition="50% 50%";
		bckg.style.backgroundSize="cover";
		vid=document.getElementById("player");
		vid.className="hidden";
		 player.pauseVideo();
	}
	
	function change3(){
		var img,bckg,vid;
		img = document.getElementById("img");
		img.src="main/socini/envday.jpg";
		img.className="visible";
		bckg = document.getElementById("socini");
		bckg.style.background='url(images/socini/envday.jpg)';
		bckg.style.backgroundPosition="50% 50%";
		bckg.style.backgroundSize="cover";
		vid=document.getElementById("player");
		vid.className="hidden";
		 player.pauseVideo();
	}
	
	function change4(){
		var img,bckg,vid;
		img = document.getElementById("img");
		img.src="images/socini/childlabor.jpg";
		img.className="hidden";
		vid=document.getElementById("player");
		vid.className="visible";
		bckg = document.getElementById("socini");
		bckg.style.background='url(images/socini/childlabor.jpg)';
		bckg.style.backgroundPosition="50% 50%";
		bckg.style.backgroundSize="cover";
		   player.pauseVideo();
	}

    function change5(){
		var img,bckg,vid;
		img = document.getElementById("img");
		img.src="images/socini/socinititle.jpg";
		img.className="visible";
		bckg = document.getElementById("socini");
		bckg.style.background='url(images/socini/title.jpg)';
		bckg.style.backgroundPosition="50% 50%";
		bckg.style.backgroundSize="cover";
		vid=document.getElementById("player");
		vid.className="hidden";
		 player.pauseVideo();
	}
