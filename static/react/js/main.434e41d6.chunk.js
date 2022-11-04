(this["webpackJsonpfleet-simulator"]=this["webpackJsonpfleet-simulator"]||[]).push([[0],{162:function(e,t,n){},166:function(e,t){},170:function(e,t,n){"use strict";n.r(t);var i=n(4),a=n.n(i),c=n(121),o=n.n(c),r=(n(162),n(0)),s=n(17),l=n(13),d=n(143),u=n(137),p=n(179),b=n(125),j=n(186),g=n(185),x=n(188),m=n(110),f=n(146),h=n(19);var v=new u.a({color:[255,255,255],intensity:1}),O=new p.a({color:[255,255,255],intensity:2,position:[-74.762758,40.226667,8e3]}),_={buildingColor:[175,175,175],trailColor0:[255,0,0],trailColor1:[230,140,0],trailColor2:[200,200,0],trailColor3:[60,200,0],trailColor4:[0,100,0],material:{ambient:.1,diffuse:.6,shininess:32,specularColor:[60,64,70]},effects:[new b.a({ambientLight:v,pointLight:O})]},k={longitude:center_coordinates.lng,latitude:center_coordinates.lat,zoom:12,pitch:45,bearing:0},S={marker:{x:0,y:0,width:512,height:512,anchorY:512}};var y=function(e){var t=e.kiosks,n=void 0===t?KIOSKS:t,a=e.kiosk_metrics,c=void 0===a?KIOSK_METRICS:a,o=e.road_network,u=void 0===o?ROAD_NETWORK:o,p=e.trips,b=void 0===p?TRIPS:p,v=e.trailLength,O=void 0===v?10:v,y=e.initialViewState,w=void 0===y?k:y,P=e.mapStyle,C=void 0===P?"https://basemaps.cartocdn.com/gl/positron-gl-style/style.json":P,I=e.theme,T=void 0===I?_:I,L=e.loopLength,M=void 0===L?LOOP_LENGTH:L,E=e.startingAnimationSpeed,z=void 0===E?1:E,A=e.startTime,F=void 0===A?0:A,B=Object(i.useState)([]),K=Object(l.a)(B,2),R=K[0],W=K[1],D=Object(i.useState)(z),q=Object(l.a)(D,2),J=q[0],N=q[1],V=Object(i.useState)(J),G=Object(l.a)(V,2),H=G[0],Y=G[1],Z=Object(i.useState)(F),Q=Object(l.a)(Z,2),U=Q[0],X=Q[1];!function(e){var t="AM";e/3600>=12&&(t="PM"),e/3600<=6||e/3600>=18?($("#time").css("background-color","black"),$("#time").css("color","white")):($("#time").css("background-color","white"),$("#time").css("color","black"));var n=Math.floor(e/3600)%12,i=Math.floor(e/60)%60,a=e%60;0==n&&(n=12),n=n<10?"0".concat(n):n,i=i<10?"0".concat(i):i,a=a<10?"0".concat(a):a;var c="".concat(n,":").concat(i,":").concat(a," ").concat(t);$("#time").text(c)}(U),function(e){var t=(e-e%TIME_STEP).toString(),n=timeframe_metrics[t].vehicles_moving;$("#vehicles_moving").text(n.toLocaleString());var i=timeframe_metrics[t].vehicles_with_pax_moving;$("#vehicles_with_pax_moving").text(i.toLocaleString());var a=timeframe_metrics[t].empty_vehicles_moving;$("#empty_vehicles_moving").text(a.toLocaleString());var c=timeframe_metrics[t].vehicles_not_moving;$("#vehicles_not_moving").text(c.toLocaleString());var o=timeframe_metrics[t].total_pax;$("#total_pax").text(o.toLocaleString());var r=timeframe_metrics[t].pax_moving;$("#pax_moving").text(r.toLocaleString());var s=timeframe_metrics[t].pax_waiting;$("#pax_waiting").text(s.toLocaleString());var l=timeframe_metrics[t].pax_served_running_total;$("#pax_served_running_total").text(l.toLocaleString());var d=timeframe_metrics[t].pax_missed_running_total;$("#pax_missed_running_total").text(d.toLocaleString())}(U);var ee=Object(i.useState)({}),te=Object(l.a)(ee,1)[0],ne=function e(){X((function(e){return(e+J)%M})),te.id=window.requestAnimationFrame(e)};Object(i.useEffect)((function(){return te.id=window.requestAnimationFrame(ne),function(){return window.cancelAnimationFrame(te.id)}}),[te,J,U,H,R]);var ie=[T.trailColor0,T.trailColor1,T.trailColor2,T.trailColor3,T.trailColor4],ae=[new x.a({id:"road-network",data:u,pickable:!1,lineWidthScale:20,getLineWidth:1,lineWidthMinPixels:2,getLineColor:[169,169,169,100],parameters:{depthTest:!1}}),new m.a({id:"icon-layer",data:n,pickable:!0,iconAtlas:"/static/assets/kiosk_clipart.png",iconMapping:S,getIcon:function(e){return"marker"},sizeScale:5,getPosition:function(e){return e.coordinates},getSize:function(e){return 5},sizeMinPixels:20,sizeMaxPixels:200,parameters:{depthTest:!1}}),new f.a({id:"vehicle-passenger-counts",data:c[(U-U%TIME_STEP).toString()],pickable:!1,fontFamily:"monospace, Material Icons",characterSet:["\ue559","\ue7fd","\uf233","0","1","2","3","4","5","6","7","8","9",",","\n"],getPosition:function(e){return e.c},getText:function(e){return e.n+"\n"+e.v.toLocaleString()+"\ue559 "+e.p.toLocaleString()+"\ue7fd "+e.g.toLocaleString()+"\uf233"},getSize:15,getAngle:0,getTextAnchor:"middle",getAlignmentBaseline:"top",parameters:{depthTest:!1}}),new g.a({id:"trips",data:b,getPath:function(e){return e.lnglats},getTimestamps:function(e){return e.timestamps},getColor:function(e){var t=e.num_passengers;return R.includes(t)?[0,0,0,0]:ie[t]},updateTriggers:{getColor:R},opacity:1,widthMinPixels:10,rounded:!0,trailLength:O,currentTime:U,shadowEnabled:!1,pickable:!0})];return Object(h.jsxs)("div",{children:[Object(h.jsx)("div",{id:"car_occupancy",style:{position:"absolute",bottom:"10px",right:"0",zIndex:"1"},children:Object(h.jsxs)("div",{class:"my-legend",children:[Object(h.jsx)("div",{class:"legend-title",children:"Car Occupancy"}),Object(h.jsx)("div",{class:"legend-scale",children:Object(h.jsxs)("ul",{class:"legend-labels",children:[Object(h.jsxs)("li",{children:[Object(h.jsx)("input",{type:"checkbox",id:"zeroPax",value:"0",onClick:function(){var e="#zeroPax",t=Object(s.a)(R),n=[];n=$(e).prop("checked")?t.filter((function(t){return t!=parseInt($(e).val())})):t.concat(parseInt($(e).val())),W(n)}}),Object(h.jsxs)("label",{for:"zeroPax",children:[Object(h.jsx)("span",{style:{background:"rgb(255, 0, 0)"}}),"Zero Passengers"]})]}),Object(h.jsxs)("li",{children:[Object(h.jsx)("input",{type:"checkbox",id:"onePax",value:"1",onClick:function(){var e="#onePax",t=Object(s.a)(R),n=[];n=$(e).prop("checked")?t.filter((function(t){return t!=parseInt($(e).val())})):t.concat(parseInt($(e).val())),W(n)}}),Object(h.jsxs)("label",{for:"onePax",children:[Object(h.jsx)("span",{style:{background:"rgb(230, 140, 0)"}}),"One Passenger"]})]}),Object(h.jsxs)("li",{children:[Object(h.jsx)("input",{type:"checkbox",id:"twoPax",value:"2",onClick:function(){var e="#twoPax",t=Object(s.a)(R),n=[];n=$(e).prop("checked")?t.filter((function(t){return t!=parseInt($(e).val())})):t.concat(parseInt($(e).val())),W(n)}}),Object(h.jsxs)("label",{for:"twoPax",children:[Object(h.jsx)("span",{style:{background:"rgb(200, 200, 0)"}}),"Two Passengers"]})]}),Object(h.jsxs)("li",{children:[Object(h.jsx)("input",{type:"checkbox",id:"threePax",value:"3",onClick:function(){var e="#threePax",t=Object(s.a)(R),n=[];n=$(e).prop("checked")?t.filter((function(t){return t!=parseInt($(e).val())})):t.concat(parseInt($(e).val())),W(n)}}),Object(h.jsxs)("label",{for:"threePax",children:[Object(h.jsx)("span",{style:{background:"rgb(60, 200, 0)"}}),"Three Passengers"]})]}),Object(h.jsxs)("li",{children:[Object(h.jsx)("input",{type:"checkbox",id:"fourPax",value:"4",onClick:function(){var e="#fourPax",t=Object(s.a)(R),n=[];n=$(e).prop("checked")?t.filter((function(t){return t!=parseInt($(e).val())})):t.concat(parseInt($(e).val())),W(n)}}),Object(h.jsxs)("label",{for:"fourPax",children:[Object(h.jsx)("span",{style:{background:"rgb(0, 100, 0)"}}),"Four Passengers"]})]})]})})]})}),Object(h.jsxs)("div",{style:{position:"absolute",bottom:"0",left:"30%",width:"40%",textAlign:"center",zIndex:"2"},children:[Object(h.jsx)("button",{onClick:function(){X(Math.max(0,U-1))},children:Object(h.jsx)("i",{class:"fas fa-step-backward"})}),Object(h.jsx)("button",{onClick:function(){N(H)},children:Object(h.jsx)("i",{class:"fa fa-play"})}),Object(h.jsx)("button",{id:"stop_animation_button",onClick:function(){Y(J),N(0)},children:Object(h.jsx)("i",{class:"fa fa-stop"})}),Object(h.jsx)("button",{onClick:function(){X((U+1)%M)},children:Object(h.jsx)("i",{class:"fas fa-step-forward"})}),Object(h.jsx)("button",{onClick:function(){Y(1),N(1),X(0)},children:Object(h.jsx)("i",{class:"fas fa-redo"})}),Object(h.jsx)("br",{}),Object(h.jsxs)("label",{for:"speedInput",children:["Speed: ",J,"x"]}),Object(h.jsx)("input",Object(r.a)({style:{paddingTop:"5px",width:"70%",float:"right"},id:"speedInput",onChange:function(){N(parseInt(document.getElementById("speedSelector").value)),Y(parseInt(document.getElementById("speedSelector").value))},type:"range",value:J,min:"0",max:"50"},"id","speedSelector")),Object(h.jsx)("br",{}),Object(h.jsxs)("label",{for:"timeInput",children:["Time: ",U," sec"]}),Object(h.jsx)("input",Object(r.a)({style:{width:"70%",float:"right"},id:"timeInput",onChange:function(){X(parseInt(document.getElementById("timeSelector").value)%M)},type:"range",value:U,min:"0",max:M},"id","timeSelector"))]}),Object(h.jsx)(j.a,{layers:ae,effects:T.effects,initialViewState:w,controller:!0,getTooltip:function(e){var t=e.object;return t&&"".concat(t.msg)},children:Object(h.jsx)(d.a,{reuseMaps:!0,mapStyle:C,preventStyleDiffing:!0})})]})},w=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,192)).then((function(t){var n=t.getCLS,i=t.getFID,a=t.getFCP,c=t.getLCP,o=t.getTTFB;n(e),i(e),a(e),c(e),o(e)}))};o.a.render(Object(h.jsx)(a.a.StrictMode,{children:Object(h.jsx)(y,{})}),document.getElementById("root")),w()},96:function(e,t){}},[[170,1,2]]]);
//# sourceMappingURL=main.434e41d6.chunk.js.map