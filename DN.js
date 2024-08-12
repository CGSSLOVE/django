function daynight(e){
		var va1=e.value;
		var sector =document.querySelector('body').style;
		var link = document.querySelectorAll('#main_down_text>ol>li>a');
		if(va1=="night"){
			e.value="day";
			sector.backgroundColor="black";
			sector.color="white";
			for(i=0;i<link.length;i++){
				link[i].style.color="white"
			}
		}
		else if(va1=="day"){
			e.value="night";
			sector.backgroundColor="white";
			sector.color="black";
			for(i=0;i<link.length;i++){
				link[i].style.color="black"
			}
		}
		else {
			alert("오류");
		}
	}
var fc1 = {
	check:function(e){
	var scp1=e.value;	
		if (scp1==""){
		alert("값이 입력되지 않았습니다.");
		return;
		}
	var str=scp1.replace(/\s/gi,'').toUpperCase();
		if(this.songlist.findIndex(index=>index==str)>-1){
		alert(scp1+"(은/는) 이세계 아이돌의 노래가 맞습니다.");
		}
		else{
		alert(scp1+"(은/는) 이세계 아이돌의 노래가 아닙니다.");
		}
	},
	songlist:['LOCKDOWN','KIDDING','ANOTHERWORLD','REWIND','RE:WIND','WINTERSPRING','OVER','SUPERHERO','BUTYOUWANTMORE','ISEGYEIDOLCYPHER','리와인드','겨울봄','키딩','락다운','어나더월드',
	       '오버','슈퍼히어로','버츄원몰','이세계아이돌싸이퍼','이세돌싸이퍼'],
};
