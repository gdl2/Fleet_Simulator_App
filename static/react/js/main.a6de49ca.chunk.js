(this["webpackJsonpfleet-simulator"]=this["webpackJsonpfleet-simulator"]||[]).push([[0],{160:function(e,t,n){},164:function(e,t){},168:function(e,t,n){"use strict";n.r(t);var i=n(4),o=n.n(i),c=n(120),a=n.n(c),s=(n(160),n(0)),r=n(17),l=n(13),d=n(142),u=n(136),b=n(177),j=n(124),p=n(184),g=n(188),f=n(186),O=n(191),x=n(178),h=n(19);var m=new u.a({color:[255,255,255],intensity:1}),v=new b.a({color:[255,255,255],intensity:2,position:[-74.762758,40.226667,8e3]}),I={buildingColor:[175,175,175],trailColor0:[255,0,0],trailColor1:[173,216,230],trailColor2:[0,0,139],trailColor3:[144,238,144],trailColor4:[0,100,0],material:{ambient:.1,diffuse:.6,shininess:32,specularColor:[60,64,70]},effects:[new j.a({ambientLight:m,pointLight:v})]},S={longitude:VIEWSTATE_COORDINATES[1],latitude:VIEWSTATE_COORDINATES[0],zoom:12,pitch:45,bearing:0};var P=function(e){var t=e.buildings,n=void 0===t?BUILDINGS:t,o=e.depot_locations,c=void 0===o?DEPOT_LOCATIONS:o,a=e.trips,u=void 0===a?TRIPS:a,b=e.missed_passengers,j=void 0===b?MISSED_PASSENGERS:b,m=e.waiting,v=void 0===m?WAITING:m,P=e.trailLength,C=void 0===P?15:P,T=e.initialViewState,A=void 0===T?S:T,y=e.mapStyle,k=void 0===y?"https://basemaps.cartocdn.com/gl/positron-nolabels-gl-style/style.json":y,w=e.theme,E=void 0===w?I:w,M=e.loopLength,N=void 0===M?LOOP_LENGTH:M,_=e.startingAnimationSpeed,F=void 0===_?ANIMATION_SPEED:_,L=e.startTime,R=void 0===L?START_TIME:L,D=Object(i.useState)([]),B=Object(l.a)(D,2),z=B[0],V=B[1],G=Object(i.useState)(F),W=Object(l.a)(G,2),q=W[0],J=W[1],H=Object(i.useState)(q),U=Object(l.a)(H,2),Z=U[0],K=U[1],Q=Object(i.useState)(R),X=Object(l.a)(Q,2),Y=X[0],ee=X[1];!function(e){var t="AM";e/3600>=12&&(t="PM"),e/3600<=6||e/3600>=18?($("#time").css("background-color","black"),$("#time").css("color","white")):($("#time").css("background-color","white"),$("#time").css("color","black"));var n=Math.floor(e/3600)%12,i=Math.floor(e/60)%60,o=e%60;0==n&&(n=12),n=n<10?"0".concat(n):n,i=i<10?"0".concat(i):i,o=o<10?"0".concat(o):o;var c="".concat(n,":").concat(i,":").concat(o," ").concat(t);$("#time").text(c)}(Y),function(e){var t=METRIC_ANIMATIONS.NumOfActiveVehicles[e],n=METRIC_ANIMATIONS.NumOfActivePassengers[e],i=METRIC_ANIMATIONS.AVO[e],o=METRIC_ANIMATIONS.PassengersLeft[e],c=METRIC_ANIMATIONS.ServedPassengers[e];$("#AVO").html(i.toFixed(2).toString()),$("#NumOfActiveVehicles").html(t.toString()),$("#NumOfActivePassengers").html(n.toString()),$("#PassengersLeft").html(o.toString()),$("#ServedPassengers").html(c.toString())}(Y);var te=Object(i.useState)({}),ne=Object(l.a)(te,1)[0],ie=function e(){ee((function(e){return(e+q)%N})),ne.id=window.requestAnimationFrame(e)};Object(i.useEffect)((function(){return ne.id=window.requestAnimationFrame(ie),function(){return window.cancelAnimationFrame(ne.id)}}),[ne,q,Y,Z,z]);var oe=c,ce=[E.trailColor0,E.trailColor1,E.trailColor2,E.trailColor3,E.trailColor4],ae=[new x.a({id:"trips",data:u,getPath:function(e){return e.path},getTimestamps:function(e){return e.timestamps},getColor:function(e){var t=e.vendor;return z.includes(t)?[0,0,0,0]:ce[t]},updateTriggers:{getColor:z},opacity:1,widthMinPixels:10,rounded:!0,trailLength:C,currentTime:Y,shadowEnabled:!1,pickable:!0}),new g.a({id:"buildings",data:n,extruded:!0,wireframe:!1,opacity:.5,getPolygon:function(e){return e.polygon},getElevation:function(e){return e.height},getFillColor:E.buildingColor,material:E.material,pickable:!0}),new f.a({id:"waiting_passengers",data:v[Y],getPosition:function(e){return oe[e.c.split(" ")[0]]},getText:function(e){return e.c.split(" ")[1]},getSize:20,getColor:[255,0,0],getTextAnchor:"start",getAlignmentBaseline:"bottom",getPixelOffset:[5,5],parameters:{depthTest:!1}}),new f.a({id:"waiting_vehicles",data:v[Y],getPosition:function(e){return oe[e.c.split(" ")[0]]},getText:function(e){return e.c.split(" ")[2]},getSize:20,getColor:[79,130,247],getTextAnchor:"end",getAlignmentBaseline:"bottom",getPixelOffset:[-5,5],parameters:{depthTest:!1}}),new O.a({id:"missed_passengers",data:j[Y],getPosition:function(e){return oe[e.c]},getRadius:100,filled:!0,getFillColor:[255,0,0],opacity:.5,radiusMinPixels:1,radiusMaxPixels:200,parameters:{depthTest:!1},pickable:!0})];return Object(h.jsxs)("div",{children:[Object(h.jsx)("div",{id:"topright",style:{position:"absolute",bottom:"10px",right:"0",zIndex:"1"},children:Object(h.jsxs)("div",{class:"my-legend",children:[Object(h.jsx)("div",{class:"legend-title",children:"Car Occupancy"}),Object(h.jsx)("div",{class:"legend-scale",children:Object(h.jsxs)("ul",{class:"legend-labels",children:[Object(h.jsxs)("li",{children:[Object(h.jsx)("input",{type:"checkbox",id:"zeroPax",value:"0",onClick:function(){var e="#zeroPax",t=Object(r.a)(z),n=[];n=$(e).prop("checked")?t.filter((function(t){return t!=parseInt($(e).val())})):t.concat(parseInt($(e).val())),console.log(n),V(n)}}),Object(h.jsxs)("label",{for:"zeroPax",children:[Object(h.jsx)("span",{style:{background:"#FF0000"}}),"Zero Passengers"]})]}),Object(h.jsxs)("li",{children:[Object(h.jsx)("input",{type:"checkbox",id:"onePax",value:"1",onClick:function(){var e="#onePax",t=Object(r.a)(z),n=[];n=$(e).prop("checked")?t.filter((function(t){return t!=parseInt($(e).val())})):t.concat(parseInt($(e).val())),console.log(n),V(n)}}),Object(h.jsxs)("label",{for:"onePax",children:[Object(h.jsx)("span",{style:{background:"#ADD8E6"}}),"One Passenger"]})]}),Object(h.jsxs)("li",{children:[Object(h.jsx)("input",{type:"checkbox",id:"twoPax",value:"2",onClick:function(){var e="#twoPax",t=Object(r.a)(z),n=[];n=$(e).prop("checked")?t.filter((function(t){return t!=parseInt($(e).val())})):t.concat(parseInt($(e).val())),console.log(n),V(n)}}),Object(h.jsxs)("label",{for:"twoPax",children:[Object(h.jsx)("span",{style:{background:"#00008B"}}),"Two Passengers"]})]}),Object(h.jsxs)("li",{children:[Object(h.jsx)("input",{type:"checkbox",id:"threePax",value:"3",onClick:function(){var e="#threePax",t=Object(r.a)(z),n=[];n=$(e).prop("checked")?t.filter((function(t){return t!=parseInt($(e).val())})):t.concat(parseInt($(e).val())),console.log(n),V(n)}}),Object(h.jsxs)("label",{for:"threePax",children:[Object(h.jsx)("span",{style:{background:"#90EE90"}}),"Three Passengers"]})]}),Object(h.jsxs)("li",{children:[Object(h.jsx)("input",{type:"checkbox",id:"fourPax",value:"4",onClick:function(){var e="#fourPax",t=Object(r.a)(z),n=[];n=$(e).prop("checked")?t.filter((function(t){return t!=parseInt($(e).val())})):t.concat(parseInt($(e).val())),console.log(n),V(n)}}),Object(h.jsxs)("label",{for:"fourPax",children:[Object(h.jsx)("span",{style:{background:"#006400"}}),"Four Passengers"]})]})]})})]})}),Object(h.jsxs)("div",{style:{position:"absolute",bottom:"0",left:"30%",width:"40%",textAlign:"center",zIndex:"2"},children:[Object(h.jsx)("button",{onClick:function(){ee(Math.max(0,Y-1))},children:Object(h.jsx)("i",{class:"fas fa-step-backward"})}),Object(h.jsx)("button",{onClick:function(){J(Z)},children:Object(h.jsx)("i",{class:"fa fa-play"})}),Object(h.jsx)("button",{onClick:function(){K(q),J(0)},children:Object(h.jsx)("i",{class:"fa fa-stop"})}),Object(h.jsx)("button",{onClick:function(){ee((Y+1)%N)},children:Object(h.jsx)("i",{class:"fas fa-step-forward"})}),Object(h.jsx)("button",{onClick:function(){K(1),J(1),ee(0)},children:Object(h.jsx)("i",{class:"fas fa-redo"})}),Object(h.jsx)("br",{}),Object(h.jsxs)("label",{for:"speedInput",children:["Speed: ",q,"x"]}),Object(h.jsx)("input",Object(s.a)({style:{paddingTop:"5px",width:"70%",float:"right"},id:"speedInput",onChange:function(){J(parseInt(document.getElementById("speedSelector").value)),K(parseInt(document.getElementById("speedSelector").value))},type:"range",value:q,min:"0",max:"50"},"id","speedSelector")),Object(h.jsx)("br",{}),Object(h.jsxs)("label",{for:"timeInput",children:["Time: ",Y," sec"]}),Object(h.jsx)("input",Object(s.a)({style:{width:"70%",float:"right"},id:"timeInput",onChange:function(){ee(parseInt(document.getElementById("timeSelector").value)%N)},type:"range",value:Y,min:"0",max:N},"id","timeSelector"))]}),Object(h.jsx)(p.a,{layers:ae,effects:E.effects,initialViewState:A,controller:!0,getTooltip:function(e){var t=e.object;return t&&t.m},children:Object(h.jsx)(d.a,{reuseMaps:!0,mapStyle:k,preventStyleDiffing:!0})})]})},C=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,192)).then((function(t){var n=t.getCLS,i=t.getFID,o=t.getFCP,c=t.getLCP,a=t.getTTFB;n(e),i(e),o(e),c(e),a(e)}))};a.a.render(Object(h.jsx)(o.a.StrictMode,{children:Object(h.jsx)(P,{})}),document.getElementById("root")),C()},96:function(e,t){}},[[168,1,2]]]);
//# sourceMappingURL=main.a6de49ca.chunk.js.map