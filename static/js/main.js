

function displayGraph(event){
    
    const region =event.target.textContent;
    const initialPath='../../static/media'
    const rLosspath=`${initialPath}/${region}/revenueLoss.png`;
    const pgrowthpath=`${initialPath}/${region}/psizeGrowth.png`;
    const setparamspath=`${initialPath}/${region}/setParams.png`;
    const topvendor1=`${initialPath}/${region}/topvendor1.png`;
    const topvendor2=`${initialPath}/${region}/topvendor2.png`;

    document.getElementById('region').innerHTML=region;

    document.getElementById('rloss').src=rLosspath;
    document.getElementById('pgrowth').src=pgrowthpath;
    document.getElementById('setparams').src=setparamspath;
    document.getElementById('tvendorup').src=topvendor1;
    document.getElementById('tvendordown').src=topvendor2;
}

function closeDashboard(){
    document.getElementById('side_nav').style.display='none';
    document.getElementById('dash_open').style.display='block';
}

function openDashboard(){
    document.getElementById('side_nav').style.display='block';
    document.getElementById('dash_open').style.display='none'
}

