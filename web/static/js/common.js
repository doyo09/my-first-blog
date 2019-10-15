$(document).ready(function () {

  /*
  메뉴 관련 JS
  */
  var menuHtml = `
  <div id="menuBox">
    <a href="https://gonggongplace.com/"><img src="/static/img/logo.png" id="logo"/></a>
    <div class="menu_box">
      <a href="/" class="main_title">공공블록</a>
    </div>
    <div class="menu_box on">
      <a href="/wallet" class="main_title">지갑</a>
    </div>
    <div class="menu_box">
      <a href="/transaction" class="main_title">트랜잭션</a>
    </div>
    <div class="menu_box">
      <a href="/mining" class="main_title">마이닝</a>
    </div>
    <div class="menu_box">
      <a href="/block" class="main_title">블록</a>
    </div>
  </div>
  `;

  /*
    <div class="menu_box">
      <a href="/story" class="main_title">오픈예정</a>
    </div>
    <div class="menu_box">
      <a href="/realEstate" class="main_title">부동산</a>
    </div>
  */

  var url = window.location.href;

  if(url.indexOf("block") > -1){
    menuHtml += `
    <div class="sub_menu">
      <a href="" class="sub_title">조회</a>
    </div>
    `;
  }else if(url.indexOf("story") > -1){
    menuHtml += `
    <div class="sub_menu">
      <a href="" class="sub_title">조회</a>
    </div>
    `;
  }else if(url.indexOf("realEstate") > -1){
    menuHtml += `
    <div class="sub_menu">
      <a href="" class="sub_title">시세조회</a>
    </div>
    `;
  }else if(url.indexOf("mining") > -1){
    menuHtml += `
    <div class="sub_menu">
      <a href="" class="sub_title">New block</a>
    </div>
    `;
  }else if(url.indexOf("transaction") > -1){
    menuHtml += `
    <div class="sub_menu">
      <a href="" class="sub_title">New Tx</a>
    </div>
    `;
  }else if(url.indexOf("wallet") > -1){
    menuHtml += `
    <div class="sub_menu">
      <a href="/wallet" class="sub_title">Bitcoin Keys</a>
      <a href="/wallet_ether" class="sub_title">Ethereum Keys</a>
    </div>
    `;
  }else{
    menuHtml += `
    <div class="sub_menu">
      <a href="" class="sub_title">Home</a>
    </div>
    `;
  }

  $("#top").html(menuHtml);
});
