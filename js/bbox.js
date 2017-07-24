document.write('<!DOCTYPE html>
<head>    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <script>L_PREFER_CANVAS = false; L_NO_TOUCH = false; L_DISABLE_3D = false;</script>
    <script src="https://unpkg.com/leaflet@1.0.1/dist/leaflet.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.0.0/leaflet.markercluster-src.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.0.0/leaflet.markercluster.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.1/dist/leaflet.css" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.0.0/MarkerCluster.Default.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.0.0/MarkerCluster.css" />
    <link rel="stylesheet" href="https://rawgit.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css" />
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    
            <style> #map_e9b6ee2bda63442881c2e83926db41bd {
                position : relative;
                width : 100.0%;
                height: 100.0%;
                left: 0.0%;
                top: 0.0%;
                }
            </style>
        
</head>
<body>    
    
            <div class="folium-map" id="map_e9b6ee2bda63442881c2e83926db41bd" ></div>
        
</body>
<script>    
    

            
                var southWest = L.latLng(-90, -180);
                var northEast = L.latLng(90, 180);
                var bounds = L.latLngBounds(southWest, northEast);
            

            var map_e9b6ee2bda63442881c2e83926db41bd = L.map(
                                  'map_e9b6ee2bda63442881c2e83926db41bd',
                                  {center: [55.6667,12.5833],
                                  zoom: 4,
                                  maxBounds: bounds,
                                  layers: [],
                                  worldCopyJump: false,
                                  crs: L.CRS.EPSG3857
                                 });
            L.control.scale().addTo(map_e9b6ee2bda63442881c2e83926db41bd);
        
    
            var tile_layer_c3573ddaa09848aa847d476bbae69bd9 = L.tileLayer(
                'https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png',
                {
                    maxZoom: 18,
                    minZoom: 1,
                    continuousWorld: false,
                    noWrap: false,
                    attribution: '(c) <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors (c) <a href="http://cartodb.com/attributions">CartoDB</a>, CartoDB <a href ="http://cartodb.com/attributions">attributions</a>',
                    detectRetina: false
                    }
                ).addTo(map_e9b6ee2bda63442881c2e83926db41bd);

        
    
            var tile_layer_47cada5a8ee7468bbd05c0b2afc4dfeb = L.tileLayer(
                'http://tile.openweathermap.org/map/wind_new/{z}/{x}/{y}.png?appid=93b5f916beeed282e178f687bb4473c5',
                {
                    maxZoom: 18,
                    minZoom: 1,
                    continuousWorld: false,
                    noWrap: false,
                    attribution: 'tile.openweathermap.org',
                    detectRetina: false
                    }
                ).addTo(map_e9b6ee2bda63442881c2e83926db41bd);

        
    
            var tile_layer_01765ab4b4144b3c946008bc9c74e517 = L.tileLayer(
                'http://tile.openweathermap.org/map/clouds_new/{z}/{x}/{y}.png?appid=93b5f916beeed282e178f687bb4473c5',
                {
                    maxZoom: 18,
                    minZoom: 1,
                    continuousWorld: false,
                    noWrap: false,
                    attribution: 'tile.openweathermap.org',
                    detectRetina: false
                    }
                ).addTo(map_e9b6ee2bda63442881c2e83926db41bd);

        
    
            var tile_layer_af53a5524b8b4d5f923713cc4ca20acc = L.tileLayer(
                'http://tile.openweathermap.org/map/precipitation_new/{z}/{x}/{y}.png?appid=93b5f916beeed282e178f687bb4473c5',
                {
                    maxZoom: 18,
                    minZoom: 1,
                    continuousWorld: false,
                    noWrap: false,
                    attribution: 'tile.openweathermap.org',
                    detectRetina: false
                    }
                ).addTo(map_e9b6ee2bda63442881c2e83926db41bd);

        
    
            var tile_layer_e94c1f442b1c4130bb3129be2381b720 = L.tileLayer(
                'http://tile.openweathermap.org/map/temp_new/{z}/{x}/{y}.png?appid=93b5f916beeed282e178f687bb4473c5',
                {
                    maxZoom: 18,
                    minZoom: 1,
                    continuousWorld: false,
                    noWrap: false,
                    attribution: 'tile.openweathermap.org',
                    detectRetina: false
                    }
                ).addTo(map_e9b6ee2bda63442881c2e83926db41bd);

        
    
            var marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6 = L.markerClusterGroup();
            map_e9b6ee2bda63442881c2e83926db41bd.addLayer(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

            var marker_d8f3fc43a2884d3fa1cb460542ff3a45 = L.marker(
                [54.200001,9.1],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_22b5ff5f71d54094b74a63f3b1bf7823 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_d8f3fc43a2884d3fa1cb460542ff3a45.setIcon(icon_22b5ff5f71d54094b74a63f3b1bf7823);
            
    
            var popup_a2afe63cd452482d86674bce2e68c9fb = L.popup({maxWidth: '300'});

            
                var html_ff44d8001d6f4eaa8f111ae473955e06 = $('<div id="html_ff44d8001d6f4eaa8f111ae473955e06" style="width: 100.0%; height: 100.0%;">Location: Heide, Temperature: 17.47</div>')[0];
                popup_a2afe63cd452482d86674bce2e68c9fb.setContent(html_ff44d8001d6f4eaa8f111ae473955e06);
            

            marker_d8f3fc43a2884d3fa1cb460542ff3a45.bindPopup(popup_a2afe63cd452482d86674bce2e68c9fb);

            
        
    

            var marker_7855848309324cdb9aecd37331e87d54 = L.marker(
                [54.485802,9.05239],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_140cfff16d0245c18e9098e90d84642c = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_7855848309324cdb9aecd37331e87d54.setIcon(icon_140cfff16d0245c18e9098e90d84642c);
            
    
            var popup_e9b68849c17945ea8a0a7bc22731c5d9 = L.popup({maxWidth: '300'});

            
                var html_0e572e8b632d48e59b0372eac0e13c65 = $('<div id="html_0e572e8b632d48e59b0372eac0e13c65" style="width: 100.0%; height: 100.0%;">Location: Husum, Temperature: 17.3</div>')[0];
                popup_e9b68849c17945ea8a0a7bc22731c5d9.setContent(html_0e572e8b632d48e59b0372eac0e13c65);
            

            marker_7855848309324cdb9aecd37331e87d54.bindPopup(popup_e9b68849c17945ea8a0a7bc22731c5d9);

            
        
    

            var marker_977dc31b00b44ad2a7b724bcb69cb926 = L.marker(
                [54.783329,9.43333],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_73c8e540fb4841c98fd392f20ef017f6 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_977dc31b00b44ad2a7b724bcb69cb926.setIcon(icon_73c8e540fb4841c98fd392f20ef017f6);
            
    
            var popup_20d9003e915744d49e0d8ab005bbb9ad = L.popup({maxWidth: '300'});

            
                var html_3a207ebc2bf94607a680daec4583387a = $('<div id="html_3a207ebc2bf94607a680daec4583387a" style="width: 100.0%; height: 100.0%;">Location: Flensburg, Temperature: 17.61</div>')[0];
                popup_20d9003e915744d49e0d8ab005bbb9ad.setContent(html_3a207ebc2bf94607a680daec4583387a);
            

            marker_977dc31b00b44ad2a7b724bcb69cb926.bindPopup(popup_20d9003e915744d49e0d8ab005bbb9ad);

            
        
    

            var marker_23c972bb674245c39c06e2d3d58c2f7b = L.marker(
                [54.299999,9.66667],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_ad930ca460a046a98e22f7efa46f5978 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_23c972bb674245c39c06e2d3d58c2f7b.setIcon(icon_ad930ca460a046a98e22f7efa46f5978);
            
    
            var popup_7b39c8f3938d4f04b6efeb3c49a049a8 = L.popup({maxWidth: '300'});

            
                var html_d8e35a11b99447328aac0dfd0b20f441 = $('<div id="html_d8e35a11b99447328aac0dfd0b20f441" style="width: 100.0%; height: 100.0%;">Location: Rendsburg, Temperature: 17.66</div>')[0];
                popup_7b39c8f3938d4f04b6efeb3c49a049a8.setContent(html_d8e35a11b99447328aac0dfd0b20f441);
            

            marker_23c972bb674245c39c06e2d3d58c2f7b.bindPopup(popup_7b39c8f3938d4f04b6efeb3c49a049a8);

            
        
    

            var marker_5178fbdd7c8e49e58c8e49fbdff0d0e6 = L.marker(
                [54.466671,9.83333],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_e669096de8c4477fa28044fc3198259c = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_5178fbdd7c8e49e58c8e49fbdff0d0e6.setIcon(icon_e669096de8c4477fa28044fc3198259c);
            
    
            var popup_c7f7bf416461497683587e885112eb1c = L.popup({maxWidth: '300'});

            
                var html_6d0d659f7c93423d8c68565d6c6d87c4 = $('<div id="html_6d0d659f7c93423d8c68565d6c6d87c4" style="width: 100.0%; height: 100.0%;">Location: Eckernforde, Temperature: 17.75</div>')[0];
                popup_c7f7bf416461497683587e885112eb1c.setContent(html_6d0d659f7c93423d8c68565d6c6d87c4);
            

            marker_5178fbdd7c8e49e58c8e49fbdff0d0e6.bindPopup(popup_c7f7bf416461497683587e885112eb1c);

            
        
    

            var marker_ef12fc3256014bb4bab95736a350c02e = L.marker(
                [54.51667,9.55],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_3076223e1386493494110edb67f515cc = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_ef12fc3256014bb4bab95736a350c02e.setIcon(icon_3076223e1386493494110edb67f515cc);
            
    
            var popup_daa446a4047147ef8a60ac0ba8a2976d = L.popup({maxWidth: '300'});

            
                var html_73ed9772fc9f434fbd8f6cbcc7395949 = $('<div id="html_73ed9772fc9f434fbd8f6cbcc7395949" style="width: 100.0%; height: 100.0%;">Location: Schleswig, Temperature: 17.75</div>')[0];
                popup_daa446a4047147ef8a60ac0ba8a2976d.setContent(html_73ed9772fc9f434fbd8f6cbcc7395949);
            

            marker_ef12fc3256014bb4bab95736a350c02e.bindPopup(popup_daa446a4047147ef8a60ac0ba8a2976d);

            
        
    

            var marker_cea3776422a54bab92dc5208268de287 = L.marker(
                [55.466671,8.45],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_6e781ac64f9d4467802f7a5aac41e8c1 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_cea3776422a54bab92dc5208268de287.setIcon(icon_6e781ac64f9d4467802f7a5aac41e8c1);
            
    
            var popup_0cc0e0b8bcad4093bd7269fa90004ac3 = L.popup({maxWidth: '300'});

            
                var html_1bbe40cbb03b4a3b9e57b7bc5741f26a = $('<div id="html_1bbe40cbb03b4a3b9e57b7bc5741f26a" style="width: 100.0%; height: 100.0%;">Location: Esbjerg, Temperature: 17.19</div>')[0];
                popup_0cc0e0b8bcad4093bd7269fa90004ac3.setContent(html_1bbe40cbb03b4a3b9e57b7bc5741f26a);
            

            marker_cea3776422a54bab92dc5208268de287.bindPopup(popup_0cc0e0b8bcad4093bd7269fa90004ac3);

            
        
    

            var marker_d3b9be74587d4a61b5fac9f8c050ce48 = L.marker(
                [56.13932,8.97378],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_adfbcd80946043c69dc359300054eac5 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_d3b9be74587d4a61b5fac9f8c050ce48.setIcon(icon_adfbcd80946043c69dc359300054eac5);
            
    
            var popup_a1a99c1e34dc4ed7a1e89a826f053bc3 = L.popup({maxWidth: '300'});

            
                var html_135199695ad14341a031f311ef8eb442 = $('<div id="html_135199695ad14341a031f311ef8eb442" style="width: 100.0%; height: 100.0%;">Location: Herning, Temperature: 16.53</div>')[0];
                popup_a1a99c1e34dc4ed7a1e89a826f053bc3.setContent(html_135199695ad14341a031f311ef8eb442);
            

            marker_d3b9be74587d4a61b5fac9f8c050ce48.bindPopup(popup_a1a99c1e34dc4ed7a1e89a826f053bc3);

            
        
    

            var marker_80e07b5145194ee8a1ae20656286afe6 = L.marker(
                [55.044338,9.41741],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_acfd559cf0b64eca8bdb56c3fc9741bc = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_80e07b5145194ee8a1ae20656286afe6.setIcon(icon_acfd559cf0b64eca8bdb56c3fc9741bc);
            
    
            var popup_dcd037a0d48f41659fed4f017ac21cbf = L.popup({maxWidth: '300'});

            
                var html_7a92671e5dbd4d51a25b367412c10ec5 = $('<div id="html_7a92671e5dbd4d51a25b367412c10ec5" style="width: 100.0%; height: 100.0%;">Location: Aabenraa, Temperature: 17.24</div>')[0];
                popup_dcd037a0d48f41659fed4f017ac21cbf.setContent(html_7a92671e5dbd4d51a25b367412c10ec5);
            

            marker_80e07b5145194ee8a1ae20656286afe6.bindPopup(popup_dcd037a0d48f41659fed4f017ac21cbf);

            
        
    

            var marker_6d893f430b774524a9d968bac2f9038a = L.marker(
                [55.253769,9.48982],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_86ce46bd36bd4a78b40a4f637bcad05c = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_6d893f430b774524a9d968bac2f9038a.setIcon(icon_86ce46bd36bd4a78b40a4f637bcad05c);
            
    
            var popup_9126e178ab2c4b0dae6845ade5451cb1 = L.popup({maxWidth: '300'});

            
                var html_c8262615c2664ece842b4f006b15cbdc = $('<div id="html_c8262615c2664ece842b4f006b15cbdc" style="width: 100.0%; height: 100.0%;">Location: Haderslev, Temperature: 17.33</div>')[0];
                popup_9126e178ab2c4b0dae6845ade5451cb1.setContent(html_c8262615c2664ece842b4f006b15cbdc);
            

            marker_6d893f430b774524a9d968bac2f9038a.bindPopup(popup_9126e178ab2c4b0dae6845ade5451cb1);

            
        
    

            var marker_f51b67b5109342b2a16b57b2728f7a7a = L.marker(
                [55.490398,9.47216],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_5798163814f841e6a6c4834619ec154c = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_f51b67b5109342b2a16b57b2728f7a7a.setIcon(icon_5798163814f841e6a6c4834619ec154c);
            
    
            var popup_3e56dc42e8a841aea9d26db444a84c0c = L.popup({maxWidth: '300'});

            
                var html_1f2c8de6e6d94d519a821233f2ccc00a = $('<div id="html_1f2c8de6e6d94d519a821233f2ccc00a" style="width: 100.0%; height: 100.0%;">Location: Kolding, Temperature: 17.41</div>')[0];
                popup_3e56dc42e8a841aea9d26db444a84c0c.setContent(html_1f2c8de6e6d94d519a821233f2ccc00a);
            

            marker_f51b67b5109342b2a16b57b2728f7a7a.bindPopup(popup_3e56dc42e8a841aea9d26db444a84c0c);

            
        
    

            var marker_dca59d0b6d204947bbf34c5a8b08fe11 = L.marker(
                [54.90926,9.80737],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_4de8a52d671b40d0a309ba91ca7ae1dc = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_dca59d0b6d204947bbf34c5a8b08fe11.setIcon(icon_4de8a52d671b40d0a309ba91ca7ae1dc);
            
    
            var popup_e7c2506036fd49a1b8f3f313a7c89b69 = L.popup({maxWidth: '300'});

            
                var html_354fb5bb25d54d8583277f6f66ed65af = $('<div id="html_354fb5bb25d54d8583277f6f66ed65af" style="width: 100.0%; height: 100.0%;">Location: Sonderborg, Temperature: 17.51</div>')[0];
                popup_e7c2506036fd49a1b8f3f313a7c89b69.setContent(html_354fb5bb25d54d8583277f6f66ed65af);
            

            marker_dca59d0b6d204947bbf34c5a8b08fe11.bindPopup(popup_e7c2506036fd49a1b8f3f313a7c89b69);

            
        
    

            var marker_80dfa2a7c9be4fab83cd032b813ba220 = L.marker(
                [55.70927,9.5357],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_853f26ebd6ba4d119753ba3605963892 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_80dfa2a7c9be4fab83cd032b813ba220.setIcon(icon_853f26ebd6ba4d119753ba3605963892);
            
    
            var popup_d2bc8d5545ea40b797bbddc18c2fa4bf = L.popup({maxWidth: '300'});

            
                var html_15b5e9ed64ae471a8affe2f0e6b0d306 = $('<div id="html_15b5e9ed64ae471a8affe2f0e6b0d306" style="width: 100.0%; height: 100.0%;">Location: Vejle, Temperature: 17.26</div>')[0];
                popup_d2bc8d5545ea40b797bbddc18c2fa4bf.setContent(html_15b5e9ed64ae471a8affe2f0e6b0d306);
            

            marker_80dfa2a7c9be4fab83cd032b813ba220.bindPopup(popup_d2bc8d5545ea40b797bbddc18c2fa4bf);

            
        
    

            var marker_636055723f8141c3aa2cf1ba5b1cf65f = L.marker(
                [55.565681,9.75257],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_bf63a145c124448a9914e5455730ec01 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_636055723f8141c3aa2cf1ba5b1cf65f.setIcon(icon_bf63a145c124448a9914e5455730ec01);
            
    
            var popup_69b05f69b5d347d3b1c9a3bb85561dc2 = L.popup({maxWidth: '300'});

            
                var html_a002990897134b23ad774160a37aa3f6 = $('<div id="html_a002990897134b23ad774160a37aa3f6" style="width: 100.0%; height: 100.0%;">Location: Fredericia, Temperature: 17.26</div>')[0];
                popup_69b05f69b5d347d3b1c9a3bb85561dc2.setContent(html_a002990897134b23ad774160a37aa3f6);
            

            marker_636055723f8141c3aa2cf1ba5b1cf65f.bindPopup(popup_69b05f69b5d347d3b1c9a3bb85561dc2);

            
        
    

            var marker_8d6ba8c4935c48389ff0fe74680d2a83 = L.marker(
                [56.169701,9.54508],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_0014c0d2bbf94eb5bdb5ac2c0b9b6066 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_8d6ba8c4935c48389ff0fe74680d2a83.setIcon(icon_0014c0d2bbf94eb5bdb5ac2c0b9b6066);
            
    
            var popup_7e54fd4c80b845ddb134e656e6bd8825 = L.popup({maxWidth: '300'});

            
                var html_37c3b0cbd1cd4a4db1b3512994b8f4fb = $('<div id="html_37c3b0cbd1cd4a4db1b3512994b8f4fb" style="width: 100.0%; height: 100.0%;">Location: Silkeborg, Temperature: 16.68</div>')[0];
                popup_7e54fd4c80b845ddb134e656e6bd8825.setContent(html_37c3b0cbd1cd4a4db1b3512994b8f4fb);
            

            marker_8d6ba8c4935c48389ff0fe74680d2a83.bindPopup(popup_7e54fd4c80b845ddb134e656e6bd8825);

            
        
    

            var marker_63a84158e2f044b4a2046c36ce6ab674 = L.marker(
                [54.066669,9.98333],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_6f9e15cf21144cbb8df7373a41e39298 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_63a84158e2f044b4a2046c36ce6ab674.setIcon(icon_6f9e15cf21144cbb8df7373a41e39298);
            
    
            var popup_568ac925e51d460a8f18271c73ed0ff2 = L.popup({maxWidth: '300'});

            
                var html_223e1f2a5e40437a8d9cdc3cde7d1244 = $('<div id="html_223e1f2a5e40437a8d9cdc3cde7d1244" style="width: 100.0%; height: 100.0%;">Location: Neumunster, Temperature: 17.42</div>')[0];
                popup_568ac925e51d460a8f18271c73ed0ff2.setContent(html_223e1f2a5e40437a8d9cdc3cde7d1244);
            

            marker_63a84158e2f044b4a2046c36ce6ab674.bindPopup(popup_568ac925e51d460a8f18271c73ed0ff2);

            
        
    

            var marker_82cc88d055d846188ba41901688ce704 = L.marker(
                [54.321331,10.13489],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_f549fb983f0f48f2aca95f4dc1a2a221 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_82cc88d055d846188ba41901688ce704.setIcon(icon_f549fb983f0f48f2aca95f4dc1a2a221);
            
    
            var popup_58c0417e4e5542d49ca66b77bf4b87b6 = L.popup({maxWidth: '300'});

            
                var html_31f8638457224dba9f549c9e4100c39d = $('<div id="html_31f8638457224dba9f549c9e4100c39d" style="width: 100.0%; height: 100.0%;">Location: Kiel, Temperature: 18.0</div>')[0];
                popup_58c0417e4e5542d49ca66b77bf4b87b6.setContent(html_31f8638457224dba9f549c9e4100c39d);
            

            marker_82cc88d055d846188ba41901688ce704.bindPopup(popup_58c0417e4e5542d49ca66b77bf4b87b6);

            
        
    

            var marker_e6a83c5458ad44dfb20925cf30e46eb1 = L.marker(
                [54.23333,10.28333],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_64250f6020da4e56a4fc63b3a3f01cc0 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_e6a83c5458ad44dfb20925cf30e46eb1.setIcon(icon_64250f6020da4e56a4fc63b3a3f01cc0);
            
    
            var popup_30620bd1dc1b4d0f888cc53a06c3e3b6 = L.popup({maxWidth: '300'});

            
                var html_a4fa6f56f3fe433e8e4553d2f4624288 = $('<div id="html_a4fa6f56f3fe433e8e4553d2f4624288" style="width: 100.0%; height: 100.0%;">Location: Preetz, Temperature: 17.51</div>')[0];
                popup_30620bd1dc1b4d0f888cc53a06c3e3b6.setContent(html_a4fa6f56f3fe433e8e4553d2f4624288);
            

            marker_e6a83c5458ad44dfb20925cf30e46eb1.bindPopup(popup_30620bd1dc1b4d0f888cc53a06c3e3b6);

            
        
    

            var marker_040265bbcb854385b7dc90b15c67c8c1 = L.marker(
                [54.133331,10.61667],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_939e93669dd244a58bcb21b46b5421fa = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_040265bbcb854385b7dc90b15c67c8c1.setIcon(icon_939e93669dd244a58bcb21b46b5421fa);
            
    
            var popup_ef495c75d3ea4bb5996504340724d902 = L.popup({maxWidth: '300'});

            
                var html_b1331a18ee4341abb0fd970c3b24fc86 = $('<div id="html_b1331a18ee4341abb0fd970c3b24fc86" style="width: 100.0%; height: 100.0%;">Location: Eutin, Temperature: 17.36</div>')[0];
                popup_ef495c75d3ea4bb5996504340724d902.setContent(html_b1331a18ee4341abb0fd970c3b24fc86);
            

            marker_040265bbcb854385b7dc90b15c67c8c1.bindPopup(popup_ef495c75d3ea4bb5996504340724d902);

            
        
    

            var marker_aad35fae024d4374bf9cc54ddb173d39 = L.marker(
                [54.107071,10.8145],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_8b4bc975ecce4c9384a037f6ca074d28 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_aad35fae024d4374bf9cc54ddb173d39.setIcon(icon_8b4bc975ecce4c9384a037f6ca074d28);
            
    
            var popup_28125dc347a442d08305688023fea899 = L.popup({maxWidth: '300'});

            
                var html_b0b9575130a945af9292489e1f114754 = $('<div id="html_b0b9575130a945af9292489e1f114754" style="width: 100.0%; height: 100.0%;">Location: Neustadt in Holstein, Temperature: 18.0</div>')[0];
                popup_28125dc347a442d08305688023fea899.setContent(html_b0b9575130a945af9292489e1f114754);
            

            marker_aad35fae024d4374bf9cc54ddb173d39.bindPopup(popup_28125dc347a442d08305688023fea899);

            
        
    

            var marker_eeb3e69fece746c8952e29595cbcd660 = L.marker(
                [55.395939,10.38831],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_d26dde9c66f54baf83f1bdc4baa89114 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_eeb3e69fece746c8952e29595cbcd660.setIcon(icon_d26dde9c66f54baf83f1bdc4baa89114);
            
    
            var popup_d9eb90965eaa42329d9aed63b31a5993 = L.popup({maxWidth: '300'});

            
                var html_8b1f1fa6894b4e16be6255846134e8cb = $('<div id="html_8b1f1fa6894b4e16be6255846134e8cb" style="width: 100.0%; height: 100.0%;">Location: Odense, Temperature: 17.49</div>')[0];
                popup_d9eb90965eaa42329d9aed63b31a5993.setContent(html_8b1f1fa6894b4e16be6255846134e8cb);
            

            marker_eeb3e69fece746c8952e29595cbcd660.bindPopup(popup_d9eb90965eaa42329d9aed63b31a5993);

            
        
    

            var marker_fa5eb01f29e941afac4c746a11e8a0da = L.marker(
                [55.860661,9.85034],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_4ab8d0c6bb6948728526cfa4efd3f8a4 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_fa5eb01f29e941afac4c746a11e8a0da.setIcon(icon_4ab8d0c6bb6948728526cfa4efd3f8a4);
            
    
            var popup_f4b98165ec194529a37f3ebc1572fb0f = L.popup({maxWidth: '300'});

            
                var html_132dbf2339524cbb8aa92f16954b49c7 = $('<div id="html_132dbf2339524cbb8aa92f16954b49c7" style="width: 100.0%; height: 100.0%;">Location: Horsens, Temperature: 16.75</div>')[0];
                popup_f4b98165ec194529a37f3ebc1572fb0f.setContent(html_132dbf2339524cbb8aa92f16954b49c7);
            

            marker_fa5eb01f29e941afac4c746a11e8a0da.bindPopup(popup_f4b98165ec194529a37f3ebc1572fb0f);

            
        
    

            var marker_4161bcb5ea5a4e6fb73a1e770d02a1a1 = L.marker(
                [56.156738,10.21076],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_8633c705b552428087d78e178fa0468b = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_4161bcb5ea5a4e6fb73a1e770d02a1a1.setIcon(icon_8633c705b552428087d78e178fa0468b);
            
    
            var popup_1310ff86d05c4b128fc3be66184cbbae = L.popup({maxWidth: '300'});

            
                var html_1b0025bfe5534e068a6721b319ff6bee = $('<div id="html_1b0025bfe5534e068a6721b319ff6bee" style="width: 100.0%; height: 100.0%;">Location: Arhus, Temperature: 16.45</div>')[0];
                popup_1310ff86d05c4b128fc3be66184cbbae.setContent(html_1b0025bfe5534e068a6721b319ff6bee);
            

            marker_4161bcb5ea5a4e6fb73a1e770d02a1a1.bindPopup(popup_1310ff86d05c4b128fc3be66184cbbae);

            
        
    

            var marker_541c2c299a444547a34ebf177051de05 = L.marker(
                [55.059818,10.60677],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_6409c2ca53f241b0bc4bc264eae37ec3 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_541c2c299a444547a34ebf177051de05.setIcon(icon_6409c2ca53f241b0bc4bc264eae37ec3);
            
    
            var popup_79077a2fd3a2444089101d4f420874c1 = L.popup({maxWidth: '300'});

            
                var html_d5295c710ef049e1a386e50dbbabab7b = $('<div id="html_d5295c710ef049e1a386e50dbbabab7b" style="width: 100.0%; height: 100.0%;">Location: Svendborg, Temperature: 18.0</div>')[0];
                popup_79077a2fd3a2444089101d4f420874c1.setContent(html_d5295c710ef049e1a386e50dbbabab7b);
            

            marker_541c2c299a444547a34ebf177051de05.bindPopup(popup_79077a2fd3a2444089101d4f420874c1);

            
        
    

            var marker_bf25deafafad4c59b06de90e7a156500 = L.marker(
                [55.31274,10.78964],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_50c7bfaa17fb4fc08fdaa206da72d5c5 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_bf25deafafad4c59b06de90e7a156500.setIcon(icon_50c7bfaa17fb4fc08fdaa206da72d5c5);
            
    
            var popup_94bf2e0cc66c466d8a3ec1c3e78198c5 = L.popup({maxWidth: '300'});

            
                var html_66d6676990a24c3bb0b3e45f0463a1cc = $('<div id="html_66d6676990a24c3bb0b3e45f0463a1cc" style="width: 100.0%; height: 100.0%;">Location: Nyborg, Temperature: 17.2</div>')[0];
                popup_94bf2e0cc66c466d8a3ec1c3e78198c5.setContent(html_66d6676990a24c3bb0b3e45f0463a1cc);
            

            marker_bf25deafafad4c59b06de90e7a156500.bindPopup(popup_94bf2e0cc66c466d8a3ec1c3e78198c5);

            
        
    

            var marker_59db91f434764fbda837a08115da11e4 = L.marker(
                [55.329929,11.13857],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_581c97f44f3c4256bb6497d945c5afae = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_59db91f434764fbda837a08115da11e4.setIcon(icon_581c97f44f3c4256bb6497d945c5afae);
            
    
            var popup_ac4bb494daa34d26bb25e86494610005 = L.popup({maxWidth: '300'});

            
                var html_546b35fc144249aeb26d10d429ef218c = $('<div id="html_546b35fc144249aeb26d10d429ef218c" style="width: 100.0%; height: 100.0%;">Location: Korsor, Temperature: 18.0</div>')[0];
                popup_ac4bb494daa34d26bb25e86494610005.setContent(html_546b35fc144249aeb26d10d429ef218c);
            

            marker_59db91f434764fbda837a08115da11e4.bindPopup(popup_ac4bb494daa34d26bb25e86494610005);

            
        
    

            var marker_07a7e16de8544d5a9125a9dca3ae9f1f = L.marker(
                [55.679539,11.08864],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_b1f231e61b9d433f89de36c5d239f09f = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_07a7e16de8544d5a9125a9dca3ae9f1f.setIcon(icon_b1f231e61b9d433f89de36c5d239f09f);
            
    
            var popup_092f46f17cf949cdb86e4cc0d7894b17 = L.popup({maxWidth: '300'});

            
                var html_ebe383096c5c4e4db6c9b99ea45da6be = $('<div id="html_ebe383096c5c4e4db6c9b99ea45da6be" style="width: 100.0%; height: 100.0%;">Location: Kalundborg, Temperature: 18.0</div>')[0];
                popup_092f46f17cf949cdb86e4cc0d7894b17.setContent(html_ebe383096c5c4e4db6c9b99ea45da6be);
            

            marker_07a7e16de8544d5a9125a9dca3ae9f1f.bindPopup(popup_092f46f17cf949cdb86e4cc0d7894b17);

            
        
    

            var marker_afa0b1450dc842e7a4042afd25151bb0 = L.marker(
                [56.360088,8.61607],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_9082c134fc3d40e78ea851683b00735b = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_afa0b1450dc842e7a4042afd25151bb0.setIcon(icon_9082c134fc3d40e78ea851683b00735b);
            
    
            var popup_361fbb8008c44e05876bce7022243a06 = L.popup({maxWidth: '300'});

            
                var html_c06866b6a7e645faa5c0021be960a808 = $('<div id="html_c06866b6a7e645faa5c0021be960a808" style="width: 100.0%; height: 100.0%;">Location: Holstebro, Temperature: 16.0</div>')[0];
                popup_361fbb8008c44e05876bce7022243a06.setContent(html_c06866b6a7e645faa5c0021be960a808);
            

            marker_afa0b1450dc842e7a4042afd25151bb0.bindPopup(popup_361fbb8008c44e05876bce7022243a06);

            
        
    

            var marker_f717f0d1239843ab88d823fd81393791 = L.marker(
                [56.566669,9.03333],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_370dbeb48fec4511a785e502a0e29b55 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_f717f0d1239843ab88d823fd81393791.setIcon(icon_370dbeb48fec4511a785e502a0e29b55);
            
    
            var popup_81d1fd148a9c4e898a6af30bba8fbacf = L.popup({maxWidth: '300'});

            
                var html_fb31f23934aa4051939a06acad46582b = $('<div id="html_fb31f23934aa4051939a06acad46582b" style="width: 100.0%; height: 100.0%;">Location: Skive, Temperature: 16.0</div>')[0];
                popup_81d1fd148a9c4e898a6af30bba8fbacf.setContent(html_fb31f23934aa4051939a06acad46582b);
            

            marker_f717f0d1239843ab88d823fd81393791.bindPopup(popup_81d1fd148a9c4e898a6af30bba8fbacf);

            
        
    

            var marker_9c98bd838e4e45d5b4c619db00d75b0c = L.marker(
                [56.45319,9.40201],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_66f48cbf05c945f08ad7c54a2a63427e = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_9c98bd838e4e45d5b4c619db00d75b0c.setIcon(icon_66f48cbf05c945f08ad7c54a2a63427e);
            
    
            var popup_0d19f118195e4893a6d09fe550663b01 = L.popup({maxWidth: '300'});

            
                var html_2f21ec16a6704399ab91625ead8bfe2a = $('<div id="html_2f21ec16a6704399ab91625ead8bfe2a" style="width: 100.0%; height: 100.0%;">Location: Viborg, Temperature: 16.0</div>')[0];
                popup_0d19f118195e4893a6d09fe550663b01.setContent(html_2f21ec16a6704399ab91625ead8bfe2a);
            

            marker_9c98bd838e4e45d5b4c619db00d75b0c.bindPopup(popup_0d19f118195e4893a6d09fe550663b01);

            
        
    

            var marker_a11861536cc6417bab8c789d243d7de4 = L.marker(
                [56.466671,10.05],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_9f875d7be1a94ea1a7d41ef34ee16987 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_a11861536cc6417bab8c789d243d7de4.setIcon(icon_9f875d7be1a94ea1a7d41ef34ee16987);
            
    
            var popup_f1108b58f12641dcab96e0acd9a23282 = L.popup({maxWidth: '300'});

            
                var html_7ebd4e941da64ee19a86d41bbfc266ff = $('<div id="html_7ebd4e941da64ee19a86d41bbfc266ff" style="width: 100.0%; height: 100.0%;">Location: Randers, Temperature: 16.48</div>')[0];
                popup_f1108b58f12641dcab96e0acd9a23282.setContent(html_7ebd4e941da64ee19a86d41bbfc266ff);
            

            marker_a11861536cc6417bab8c789d243d7de4.bindPopup(popup_f1108b58f12641dcab96e0acd9a23282);

            
        
    

            var marker_1c0a2e67a421455981e5951e53d4cbb3 = L.marker(
                [57.048,9.9187],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_402e599d292b4b2eb94ba36f286f9346 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_1c0a2e67a421455981e5951e53d4cbb3.setIcon(icon_402e599d292b4b2eb94ba36f286f9346);
            
    
            var popup_32a7deb739824ced8e3e46cdc63f1119 = L.popup({maxWidth: '300'});

            
                var html_c33070fa7e704b738c7aacd75cf5fbd0 = $('<div id="html_c33070fa7e704b738c7aacd75cf5fbd0" style="width: 100.0%; height: 100.0%;">Location: Aalborg, Temperature: 15.3</div>')[0];
                popup_32a7deb739824ced8e3e46cdc63f1119.setContent(html_c33070fa7e704b738c7aacd75cf5fbd0);
            

            marker_1c0a2e67a421455981e5951e53d4cbb3.bindPopup(popup_32a7deb739824ced8e3e46cdc63f1119);

            
        
    

            var marker_edd6968078fb40c8b35df35709aec364 = L.marker(
                [57.464169,9.98229],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_3e2acfd6cfc24c9c93efc656034ceb5e = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_edd6968078fb40c8b35df35709aec364.setIcon(icon_3e2acfd6cfc24c9c93efc656034ceb5e);
            
    
            var popup_d6289bb452b44ba083f5ddf3d4f69042 = L.popup({maxWidth: '300'});

            
                var html_50c0d1834cb04c498884a2b67380ccb0 = $('<div id="html_50c0d1834cb04c498884a2b67380ccb0" style="width: 100.0%; height: 100.0%;">Location: Hjorring, Temperature: 15.4</div>')[0];
                popup_d6289bb452b44ba083f5ddf3d4f69042.setContent(html_50c0d1834cb04c498884a2b67380ccb0);
            

            marker_edd6968078fb40c8b35df35709aec364.bindPopup(popup_d6289bb452b44ba083f5ddf3d4f69042);

            
        
    

            var marker_e6b2a29924ee4dabb20668524c57b255 = L.marker(
                [57.440731,10.53661],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_658d93a4199348a2a3cebced1ae66088 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_e6b2a29924ee4dabb20668524c57b255.setIcon(icon_658d93a4199348a2a3cebced1ae66088);
            
    
            var popup_88c947dcf36a42e4a3659b46e315deb8 = L.popup({maxWidth: '300'});

            
                var html_351181223376457b96d0847c540bf440 = $('<div id="html_351181223376457b96d0847c540bf440" style="width: 100.0%; height: 100.0%;">Location: Frederikshavn, Temperature: 15.7</div>')[0];
                popup_88c947dcf36a42e4a3659b46e315deb8.setContent(html_351181223376457b96d0847c540bf440);
            

            marker_e6b2a29924ee4dabb20668524c57b255.bindPopup(popup_88c947dcf36a42e4a3659b46e315deb8);

            
        
    

            var marker_5fd16178588145838cdd206e034ca806 = L.marker(
                [54.769058,11.87425],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_e582af3396a640a88a8deac45e58fff1 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_5fd16178588145838cdd206e034ca806.setIcon(icon_e582af3396a640a88a8deac45e58fff1);
            
    
            var popup_7ce395e9d11f47629bc79784d64daafb = L.popup({maxWidth: '300'});

            
                var html_8699f222cc444196a8bb0a3b017bc77b = $('<div id="html_8699f222cc444196a8bb0a3b017bc77b" style="width: 100.0%; height: 100.0%;">Location: Nykobing Falster, Temperature: 17.4</div>')[0];
                popup_7ce395e9d11f47629bc79784d64daafb.setContent(html_8699f222cc444196a8bb0a3b017bc77b);
            

            marker_5fd16178588145838cdd206e034ca806.bindPopup(popup_7ce395e9d11f47629bc79784d64daafb);

            
        
    

            var marker_d6f349121d01451a835834fb5e8bdba3 = L.marker(
                [54.088699,12.14049],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_a525741317ff40f19f6cca1b91ea21ec = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_d6f349121d01451a835834fb5e8bdba3.setIcon(icon_a525741317ff40f19f6cca1b91ea21ec);
            
    
            var popup_bcbca44572124b089801f0653b37d2f0 = L.popup({maxWidth: '300'});

            
                var html_bf4dfa0917094364ad2bc354a3fa7e9f = $('<div id="html_bf4dfa0917094364ad2bc354a3fa7e9f" style="width: 100.0%; height: 100.0%;">Location: Rostock, Temperature: 17.0</div>')[0];
                popup_bcbca44572124b089801f0653b37d2f0.setContent(html_bf4dfa0917094364ad2bc354a3fa7e9f);
            

            marker_d6f349121d01451a835834fb5e8bdba3.bindPopup(popup_bcbca44572124b089801f0653b37d2f0);

            
        
    

            var marker_3ae47538a3c54b388a98aee9cef04eae = L.marker(
                [54.25,12.46667],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_f2353fbf9aeb42b795946ff015cd8ef2 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_3ae47538a3c54b388a98aee9cef04eae.setIcon(icon_f2353fbf9aeb42b795946ff015cd8ef2);
            
    
            var popup_73e9c9f6143d4bb4ac95f0694b40201c = L.popup({maxWidth: '300'});

            
                var html_481b02a5c6b6417891c1e586f77be3d2 = $('<div id="html_481b02a5c6b6417891c1e586f77be3d2" style="width: 100.0%; height: 100.0%;">Location: Ribnitz-Damgarten, Temperature: 17.0</div>')[0];
                popup_73e9c9f6143d4bb4ac95f0694b40201c.setContent(html_481b02a5c6b6417891c1e586f77be3d2);
            

            marker_3ae47538a3c54b388a98aee9cef04eae.bindPopup(popup_73e9c9f6143d4bb4ac95f0694b40201c);

            
        
    

            var marker_3f14709e4dfa40fcaecba6f1afd01436 = L.marker(
                [55.40276,11.35459],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_53194267ade449c8a33d3d81d6d1351f = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_3f14709e4dfa40fcaecba6f1afd01436.setIcon(icon_53194267ade449c8a33d3d81d6d1351f);
            
    
            var popup_a87249de94e04417a1998c24579f426e = L.popup({maxWidth: '300'});

            
                var html_9b792e18f31840668ca5e02c380a6e0d = $('<div id="html_9b792e18f31840668ca5e02c380a6e0d" style="width: 100.0%; height: 100.0%;">Location: Slagelse, Temperature: 18.0</div>')[0];
                popup_a87249de94e04417a1998c24579f426e.setContent(html_9b792e18f31840668ca5e02c380a6e0d);
            

            marker_3f14709e4dfa40fcaecba6f1afd01436.bindPopup(popup_a87249de94e04417a1998c24579f426e);

            
        
    

            var marker_0e676ffdfd074eeb91928ba35d5e46e6 = L.marker(
                [55.229919,11.76092],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_93731153d485467ba3ad4bde30a4cff4 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_0e676ffdfd074eeb91928ba35d5e46e6.setIcon(icon_93731153d485467ba3ad4bde30a4cff4);
            
    
            var popup_b99351c59fd84a02a9531ab8f138eed0 = L.popup({maxWidth: '300'});

            
                var html_b63346753be748d78067d61637390e08 = $('<div id="html_b63346753be748d78067d61637390e08" style="width: 100.0%; height: 100.0%;">Location: Naestved, Temperature: 18.0</div>')[0];
                popup_b99351c59fd84a02a9531ab8f138eed0.setContent(html_b63346753be748d78067d61637390e08);
            

            marker_0e676ffdfd074eeb91928ba35d5e46e6.bindPopup(popup_b99351c59fd84a02a9531ab8f138eed0);

            
        
    

            var marker_2e8769aced3a48c5ab0b91576dbd7108 = L.marker(
                [55.4426,11.79011],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_0a4d485f77fd42b881da8fd8270cd405 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_2e8769aced3a48c5ab0b91576dbd7108.setIcon(icon_0a4d485f77fd42b881da8fd8270cd405);
            
    
            var popup_cdec1dcdef63473b85c0edcd4ccd9d22 = L.popup({maxWidth: '300'});

            
                var html_edbc2a47559944409cf2c6cd020a0bbb = $('<div id="html_edbc2a47559944409cf2c6cd020a0bbb" style="width: 100.0%; height: 100.0%;">Location: Ringsted, Temperature: 18.0</div>')[0];
                popup_cdec1dcdef63473b85c0edcd4ccd9d22.setContent(html_edbc2a47559944409cf2c6cd020a0bbb);
            

            marker_2e8769aced3a48c5ab0b91576dbd7108.bindPopup(popup_cdec1dcdef63473b85c0edcd4ccd9d22);

            
        
    

            var marker_24f223b6f7ad4d499b038f5710965932 = L.marker(
                [55.716671,11.71667],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_a40d7324fba04edaa7ee70b092d7bdfb = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_24f223b6f7ad4d499b038f5710965932.setIcon(icon_a40d7324fba04edaa7ee70b092d7bdfb);
            
    
            var popup_2e74b8e60c8349ceae777532491cd541 = L.popup({maxWidth: '300'});

            
                var html_4e1b84209d744fd4bd5fec986b6ebba2 = $('<div id="html_4e1b84209d744fd4bd5fec986b6ebba2" style="width: 100.0%; height: 100.0%;">Location: Holbaek, Temperature: 18.0</div>')[0];
                popup_2e74b8e60c8349ceae777532491cd541.setContent(html_4e1b84209d744fd4bd5fec986b6ebba2);
            

            marker_24f223b6f7ad4d499b038f5710965932.bindPopup(popup_2e74b8e60c8349ceae777532491cd541);

            
        
    

            var marker_42efcc819d3346048a737f33ba31a2e8 = L.marker(
                [55.458019,12.18214],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_3a14ab61adcd418da8f0cc7cc022f999 = L.AwesomeMarkers.icon({
                    icon: 'cloud',
                    iconColor: 'white',
                    markerColor: 'lightgray',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_42efcc819d3346048a737f33ba31a2e8.setIcon(icon_3a14ab61adcd418da8f0cc7cc022f999);
            
    
            var popup_4e6c1f32ffd245dfb22b84caf59226d1 = L.popup({maxWidth: '300'});

            
                var html_bd68e7f68abd4d48b9f8ffd243b185b8 = $('<div id="html_bd68e7f68abd4d48b9f8ffd243b185b8" style="width: 100.0%; height: 100.0%;">Location: Koge, Temperature: 18.0</div>')[0];
                popup_4e6c1f32ffd245dfb22b84caf59226d1.setContent(html_bd68e7f68abd4d48b9f8ffd243b185b8);
            

            marker_42efcc819d3346048a737f33ba31a2e8.bindPopup(popup_4e6c1f32ffd245dfb22b84caf59226d1);

            
        
    

            var marker_ea65582d6cda42639fef0e2710513eb7 = L.marker(
                [55.641521,12.08035],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_93f16f332b3243c7ae1af4d30e596146 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_ea65582d6cda42639fef0e2710513eb7.setIcon(icon_93f16f332b3243c7ae1af4d30e596146);
            
    
            var popup_3dff2d301eab422881a422307324739d = L.popup({maxWidth: '300'});

            
                var html_691a60521ebc46aaab3230acc41cb625 = $('<div id="html_691a60521ebc46aaab3230acc41cb625" style="width: 100.0%; height: 100.0%;">Location: Roskilde, Temperature: 18.0</div>')[0];
                popup_3dff2d301eab422881a422307324739d.setContent(html_691a60521ebc46aaab3230acc41cb625);
            

            marker_ea65582d6cda42639fef0e2710513eb7.bindPopup(popup_3dff2d301eab422881a422307324739d);

            
        
    

            var marker_4118fba215674d1bbc59a03c1c7b9e1b = L.marker(
                [55.76828,12.19723],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_527a092557314af4b15a2634ade60ae7 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_4118fba215674d1bbc59a03c1c7b9e1b.setIcon(icon_527a092557314af4b15a2634ade60ae7);
            
    
            var popup_e80cba2327d64c6b86e6fb33c4a29c3e = L.popup({maxWidth: '300'});

            
                var html_29c9c3ad6ac54214b023c47302892908 = $('<div id="html_29c9c3ad6ac54214b023c47302892908" style="width: 100.0%; height: 100.0%;">Location: Stenlose, Temperature: 17.29</div>')[0];
                popup_e80cba2327d64c6b86e6fb33c4a29c3e.setContent(html_29c9c3ad6ac54214b023c47302892908);
            

            marker_4118fba215674d1bbc59a03c1c7b9e1b.bindPopup(popup_e80cba2327d64c6b86e6fb33c4a29c3e);

            
        
    

            var marker_5b6b5cfccef14f42be22bc96ae858d6e = L.marker(
                [55.657188,12.47364],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_9e739964d914492eb15615f3f48efe28 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_5b6b5cfccef14f42be22bc96ae858d6e.setIcon(icon_9e739964d914492eb15615f3f48efe28);
            
    
            var popup_2175042c99054845849e9bfa155ced7e = L.popup({maxWidth: '300'});

            
                var html_66e2d65e9ac1495ba25fdd0cd19e3edb = $('<div id="html_66e2d65e9ac1495ba25fdd0cd19e3edb" style="width: 100.0%; height: 100.0%;">Location: Hvidovre, Temperature: 17.23</div>')[0];
                popup_2175042c99054845849e9bfa155ced7e.setContent(html_66e2d65e9ac1495ba25fdd0cd19e3edb);
            

            marker_5b6b5cfccef14f42be22bc96ae858d6e.bindPopup(popup_2175042c99054845849e9bfa155ced7e);

            
        
    

            var marker_a459c6bbe4a74784bf2dcdd1325c1034 = L.marker(
                [55.675941,12.56553],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_203fbb71264d47f4828dd6ad2f1c9409 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_a459c6bbe4a74784bf2dcdd1325c1034.setIcon(icon_203fbb71264d47f4828dd6ad2f1c9409);
            
    
            var popup_e582a47107294dfc827c4c567b90b22d = L.popup({maxWidth: '300'});

            
                var html_1e7b409cd73c4ebea2616720f0b66121 = $('<div id="html_1e7b409cd73c4ebea2616720f0b66121" style="width: 100.0%; height: 100.0%;">Location: Copenhagen, Temperature: 16.98</div>')[0];
                popup_e582a47107294dfc827c4c567b90b22d.setContent(html_1e7b409cd73c4ebea2616720f0b66121);
            

            marker_a459c6bbe4a74784bf2dcdd1325c1034.bindPopup(popup_e582a47107294dfc827c4c567b90b22d);

            
        
    

            var marker_d3fbe5d0acf745c48783f78dcfe4433b = L.marker(
                [55.883331,12.5],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_0322b4cba4ef4b81be7965986c4f3247 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_d3fbe5d0acf745c48783f78dcfe4433b.setIcon(icon_0322b4cba4ef4b81be7965986c4f3247);
            
    
            var popup_b5c275d181554abb9a19b65a47c1009e = L.popup({maxWidth: '300'});

            
                var html_2d8d205dd6004046b0f35a45b7e9b52d = $('<div id="html_2d8d205dd6004046b0f35a45b7e9b52d" style="width: 100.0%; height: 100.0%;">Location: Horsholm, Temperature: 17.0</div>')[0];
                popup_b5c275d181554abb9a19b65a47c1009e.setContent(html_2d8d205dd6004046b0f35a45b7e9b52d);
            

            marker_d3fbe5d0acf745c48783f78dcfe4433b.bindPopup(popup_b5c275d181554abb9a19b65a47c1009e);

            
        
    

            var marker_af0e5f6730ed4d758a8c92ea14250be4 = L.marker(
                [55.75367,12.59181],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_d5752440b1fc4ba894ed7c542c133ee9 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_af0e5f6730ed4d758a8c92ea14250be4.setIcon(icon_d5752440b1fc4ba894ed7c542c133ee9);
            
    
            var popup_70eb9264881c4078bc4f1b516be99070 = L.popup({maxWidth: '300'});

            
                var html_b4c1a4f91c674943887bbd6c5d195188 = $('<div id="html_b4c1a4f91c674943887bbd6c5d195188" style="width: 100.0%; height: 100.0%;">Location: Charlottenlund, Temperature: 16.99</div>')[0];
                popup_70eb9264881c4078bc4f1b516be99070.setContent(html_b4c1a4f91c674943887bbd6c5d195188);
            

            marker_af0e5f6730ed4d758a8c92ea14250be4.bindPopup(popup_70eb9264881c4078bc4f1b516be99070);

            
        
    

            var marker_84b4fcd1154e4f4e8364535b4aa6eb60 = L.marker(
                [55.92667,12.31091],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_7bd20ab4299b41d294c01350fd22a7ca = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_84b4fcd1154e4f4e8364535b4aa6eb60.setIcon(icon_7bd20ab4299b41d294c01350fd22a7ca);
            
    
            var popup_f88f0d5efcab454198c80029141f4258 = L.popup({maxWidth: '300'});

            
                var html_1a9dbe4472eb49148465b80b4655c756 = $('<div id="html_1a9dbe4472eb49148465b80b4655c756" style="width: 100.0%; height: 100.0%;">Location: Hillerod, Temperature: 16.99</div>')[0];
                popup_f88f0d5efcab454198c80029141f4258.setContent(html_1a9dbe4472eb49148465b80b4655c756);
            

            marker_84b4fcd1154e4f4e8364535b4aa6eb60.bindPopup(popup_f88f0d5efcab454198c80029141f4258);

            
        
    

            var marker_3c2cfc6efb1f4274bab131a06f49b30a = L.marker(
                [55.8708,12.83016],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_7f49383e1d524319a70077ebdcbac17a = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_3c2cfc6efb1f4274bab131a06f49b30a.setIcon(icon_7f49383e1d524319a70077ebdcbac17a);
            
    
            var popup_ffedb559dd5b4849b5e057dccfbdce13 = L.popup({maxWidth: '300'});

            
                var html_2112bbeb17204f0b869ee235a06b4d23 = $('<div id="html_2112bbeb17204f0b869ee235a06b4d23" style="width: 100.0%; height: 100.0%;">Location: Landskrona, Temperature: 17.0</div>')[0];
                popup_ffedb559dd5b4849b5e057dccfbdce13.setContent(html_2112bbeb17204f0b869ee235a06b4d23);
            

            marker_3c2cfc6efb1f4274bab131a06f49b30a.bindPopup(popup_ffedb559dd5b4849b5e057dccfbdce13);

            
        
    

            var marker_5fac9479e51d404f8e421d801fed3a3d = L.marker(
                [56.04673,12.69437],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_825f9c83f02a4b249c826ff8b5d8b50e = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_5fac9479e51d404f8e421d801fed3a3d.setIcon(icon_825f9c83f02a4b249c826ff8b5d8b50e);
            
    
            var popup_b44edb3306404d0aab4110393c8ad747 = L.popup({maxWidth: '300'});

            
                var html_0639e63f9c4f44a7b428f882c113c962 = $('<div id="html_0639e63f9c4f44a7b428f882c113c962" style="width: 100.0%; height: 100.0%;">Location: Helsingborg, Temperature: 17.01</div>')[0];
                popup_b44edb3306404d0aab4110393c8ad747.setContent(html_0639e63f9c4f44a7b428f882c113c962);
            

            marker_5fac9479e51d404f8e421d801fed3a3d.bindPopup(popup_b44edb3306404d0aab4110393c8ad747);

            
        
    

            var marker_409dda2147034a709e4c8e5610d6a822 = L.marker(
                [56.242802,12.86219],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_97312e1dfc58423aaaa3b153dea5de85 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_409dda2147034a709e4c8e5610d6a822.setIcon(icon_97312e1dfc58423aaaa3b153dea5de85);
            
    
            var popup_0ce03b5b363b48f1a95f87f80c461286 = L.popup({maxWidth: '300'});

            
                var html_55f18302232b4d1693af317c2a2650fe = $('<div id="html_55f18302232b4d1693af317c2a2650fe" style="width: 100.0%; height: 100.0%;">Location: AEngelholm Municipality, Temperature: 16.35</div>')[0];
                popup_0ce03b5b363b48f1a95f87f80c461286.setContent(html_55f18302232b4d1693af317c2a2650fe);
            

            marker_409dda2147034a709e4c8e5610d6a822.bindPopup(popup_0ce03b5b363b48f1a95f87f80c461286);

            
        
    

            var marker_5d161b994c00469e9cc551a3978875d2 = L.marker(
                [56.905521,12.49118],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_f6d95514d4e749a597d0b13653ff15b1 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_5d161b994c00469e9cc551a3978875d2.setIcon(icon_f6d95514d4e749a597d0b13653ff15b1);
            
    
            var popup_8362005a3e0d49cc8d2664dd4e662f06 = L.popup({maxWidth: '300'});

            
                var html_d07196e56aa346b3ad77c53411793fbd = $('<div id="html_d07196e56aa346b3ad77c53411793fbd" style="width: 100.0%; height: 100.0%;">Location: Falkenberg, Temperature: 17.0</div>')[0];
                popup_8362005a3e0d49cc8d2664dd4e662f06.setContent(html_d07196e56aa346b3ad77c53411793fbd);
            

            marker_5d161b994c00469e9cc551a3978875d2.bindPopup(popup_8362005a3e0d49cc8d2664dd4e662f06);

            
        
    

            var marker_123f0c4879c34c3aa2ebb082fe02be1b = L.marker(
                [57.105572,12.25078],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_c0d313e649b646fda3e69487aad611a8 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_123f0c4879c34c3aa2ebb082fe02be1b.setIcon(icon_c0d313e649b646fda3e69487aad611a8);
            
    
            var popup_d074f578f24d489d9b2e718989c5e8b1 = L.popup({maxWidth: '300'});

            
                var html_e5b5df97f25a4fd48b0cd0397d465296 = $('<div id="html_e5b5df97f25a4fd48b0cd0397d465296" style="width: 100.0%; height: 100.0%;">Location: Varberg, Temperature: 15.49</div>')[0];
                popup_d074f578f24d489d9b2e718989c5e8b1.setContent(html_e5b5df97f25a4fd48b0cd0397d465296);
            

            marker_123f0c4879c34c3aa2ebb082fe02be1b.bindPopup(popup_d074f578f24d489d9b2e718989c5e8b1);

            
        
    

            var marker_99cef0b3140f4f24b8401dd70621513f = L.marker(
                [57.48719,12.07612],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_f524468669fb42d7a6dea86a1cdead33 = L.AwesomeMarkers.icon({
                    icon: 'asterisk',
                    iconColor: 'white',
                    markerColor: 'yellow',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_99cef0b3140f4f24b8401dd70621513f.setIcon(icon_f524468669fb42d7a6dea86a1cdead33);
            
    
            var popup_f21f1e72628a4a5398ceef3074c45720 = L.popup({maxWidth: '300'});

            
                var html_2cb0754d9da0499a8b0184c606758272 = $('<div id="html_2cb0754d9da0499a8b0184c606758272" style="width: 100.0%; height: 100.0%;">Location: Kungsbacka, Temperature: 14.0</div>')[0];
                popup_f21f1e72628a4a5398ceef3074c45720.setContent(html_2cb0754d9da0499a8b0184c606758272);
            

            marker_99cef0b3140f4f24b8401dd70621513f.bindPopup(popup_f21f1e72628a4a5398ceef3074c45720);

            
        
    

            var marker_8c424bf5fe464139b0c20a5686c5e81a = L.marker(
                [57.707161,11.96679],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_7e8ffaca682f463ba305589a3de5e386 = L.AwesomeMarkers.icon({
                    icon: 'asterisk',
                    iconColor: 'white',
                    markerColor: 'yellow',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_8c424bf5fe464139b0c20a5686c5e81a.setIcon(icon_7e8ffaca682f463ba305589a3de5e386);
            
    
            var popup_876329e94a0c4d38a3f59d894738cedc = L.popup({maxWidth: '300'});

            
                var html_0a9823f92065490497ea61a5d5af939d = $('<div id="html_0a9823f92065490497ea61a5d5af939d" style="width: 100.0%; height: 100.0%;">Location: Goeteborg, Temperature: 14.0</div>')[0];
                popup_876329e94a0c4d38a3f59d894738cedc.setContent(html_0a9823f92065490497ea61a5d5af939d);
            

            marker_8c424bf5fe464139b0c20a5686c5e81a.bindPopup(popup_876329e94a0c4d38a3f59d894738cedc);

            
        
    

            var marker_203501d79da24c07ba3361ae6c2fd35e = L.marker(
                [57.739498,12.10642],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_122fd07342f7431d82c1e1897c631288 = L.AwesomeMarkers.icon({
                    icon: 'asterisk',
                    iconColor: 'white',
                    markerColor: 'yellow',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_203501d79da24c07ba3361ae6c2fd35e.setIcon(icon_122fd07342f7431d82c1e1897c631288);
            
    
            var popup_91e6c3890de34ea19915f48105a779d6 = L.popup({maxWidth: '300'});

            
                var html_b4f269bf05234ce4a48dbf7a92e40e1e = $('<div id="html_b4f269bf05234ce4a48dbf7a92e40e1e" style="width: 100.0%; height: 100.0%;">Location: Partille, Temperature: 14.0</div>')[0];
                popup_91e6c3890de34ea19915f48105a779d6.setContent(html_b4f269bf05234ce4a48dbf7a92e40e1e);
            

            marker_203501d79da24c07ba3361ae6c2fd35e.bindPopup(popup_91e6c3890de34ea19915f48105a779d6);

            
        
    

            var marker_68c61ac442b14ee5903a5346a1993723 = L.marker(
                [57.87096,11.98054],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_df6f4fb3972f4f1aae0ab54c806c1bbd = L.AwesomeMarkers.icon({
                    icon: 'asterisk',
                    iconColor: 'white',
                    markerColor: 'yellow',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_68c61ac442b14ee5903a5346a1993723.setIcon(icon_df6f4fb3972f4f1aae0ab54c806c1bbd);
            
    
            var popup_953675ffe68b45a49d75208133a27d0f = L.popup({maxWidth: '300'});

            
                var html_bd2a8b5736ea428ea3205bbd1f1cf771 = $('<div id="html_bd2a8b5736ea428ea3205bbd1f1cf771" style="width: 100.0%; height: 100.0%;">Location: Kungalv, Temperature: 14.0</div>')[0];
                popup_953675ffe68b45a49d75208133a27d0f.setContent(html_bd2a8b5736ea428ea3205bbd1f1cf771);
            

            marker_68c61ac442b14ee5903a5346a1993723.bindPopup(popup_953675ffe68b45a49d75208133a27d0f);

            
        
    

            var marker_f24bce973a3149bb878427b70f2d9ca9 = L.marker(
                [57.770512,12.26904],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_645c338d12a5455ea80545a7e1c6e755 = L.AwesomeMarkers.icon({
                    icon: 'asterisk',
                    iconColor: 'white',
                    markerColor: 'yellow',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_f24bce973a3149bb878427b70f2d9ca9.setIcon(icon_645c338d12a5455ea80545a7e1c6e755);
            
    
            var popup_279ef66f1f774eceb89c5013b00e6d29 = L.popup({maxWidth: '300'});

            
                var html_8b714acb2bb04827a60a6f16a2f9b6a5 = $('<div id="html_8b714acb2bb04827a60a6f16a2f9b6a5" style="width: 100.0%; height: 100.0%;">Location: Lerum, Temperature: 14.0</div>')[0];
                popup_279ef66f1f774eceb89c5013b00e6d29.setContent(html_8b714acb2bb04827a60a6f16a2f9b6a5);
            

            marker_f24bce973a3149bb878427b70f2d9ca9.bindPopup(popup_279ef66f1f774eceb89c5013b00e6d29);

            
        
    

            var marker_91544183b67c40488f29a3cb295697a1 = L.marker(
                [57.930328,12.53345],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_402fe16b77ad4dbbad3a1f1446940c34 = L.AwesomeMarkers.icon({
                    icon: 'asterisk',
                    iconColor: 'white',
                    markerColor: 'yellow',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_91544183b67c40488f29a3cb295697a1.setIcon(icon_402fe16b77ad4dbbad3a1f1446940c34);
            
    
            var popup_f8e33ad6f84243dbaeda21fcfb337cad = L.popup({maxWidth: '300'});

            
                var html_445040c46577475aabd933a09b224e70 = $('<div id="html_445040c46577475aabd933a09b224e70" style="width: 100.0%; height: 100.0%;">Location: Alingsas, Temperature: 16.1</div>')[0];
                popup_f8e33ad6f84243dbaeda21fcfb337cad.setContent(html_445040c46577475aabd933a09b224e70);
            

            marker_91544183b67c40488f29a3cb295697a1.bindPopup(popup_f8e33ad6f84243dbaeda21fcfb337cad);

            
        
    

            var marker_2a2c8b2362e74ef5a5d16726de4b1945 = L.marker(
                [56.674461,12.85676],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_3c77722d71604ec9b19808b65d53eb70 = L.AwesomeMarkers.icon({
                    icon: 'tint',
                    iconColor: 'white',
                    markerColor: 'blue',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_2a2c8b2362e74ef5a5d16726de4b1945.setIcon(icon_3c77722d71604ec9b19808b65d53eb70);
            
    
            var popup_42723b92a71c4ea9a5fa54a0aa0111c8 = L.popup({maxWidth: '300'});

            
                var html_30a2c8705f0b48eab4c995dac348c388 = $('<div id="html_30a2c8705f0b48eab4c995dac348c388" style="width: 100.0%; height: 100.0%;">Location: Halmstad, Temperature: 16.46</div>')[0];
                popup_42723b92a71c4ea9a5fa54a0aa0111c8.setContent(html_30a2c8705f0b48eab4c995dac348c388);
            

            marker_2a2c8b2362e74ef5a5d16726de4b1945.bindPopup(popup_42723b92a71c4ea9a5fa54a0aa0111c8);

            
        
    

            var marker_361f0e1740d0448cbf429e85e977c15a = L.marker(
                [57.721008,12.9401],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6);
            
    

                var icon_537d0eede4204be08999a2d1650d5547 = L.AwesomeMarkers.icon({
                    icon: 'asterisk',
                    iconColor: 'white',
                    markerColor: 'yellow',
                    prefix: 'glyphicon',
                    extraClasses: 'fa-rotate-0'
                    });
                marker_361f0e1740d0448cbf429e85e977c15a.setIcon(icon_537d0eede4204be08999a2d1650d5547);
            
    
            var popup_b762811dd1624d1c9589c854ba1bf5ea = L.popup({maxWidth: '300'});

            
                var html_3043daebc8c54d3eb4d666581d7db860 = $('<div id="html_3043daebc8c54d3eb4d666581d7db860" style="width: 100.0%; height: 100.0%;">Location: Boras, Temperature: 16.13</div>')[0];
                popup_b762811dd1624d1c9589c854ba1bf5ea.setContent(html_3043daebc8c54d3eb4d666581d7db860);
            

            marker_361f0e1740d0448cbf429e85e977c15a.bindPopup(popup_b762811dd1624d1c9589c854ba1bf5ea);

            
        
    
            var layer_control_1b84a12ae2f0444893b1237e17ca9823 = {
                base_layers : { "cartodbpositron" : tile_layer_c3573ddaa09848aa847d476bbae69bd9, },
                overlays : { "wind" : tile_layer_47cada5a8ee7468bbd05c0b2afc4dfeb,"clouds" : tile_layer_01765ab4b4144b3c946008bc9c74e517,"precipitation" : tile_layer_af53a5524b8b4d5f923713cc4ca20acc,"temp" : tile_layer_e94c1f442b1c4130bb3129be2381b720,"local weather" : marker_cluster_6529bc41a8d6489eab8dac8a96b1b1f6, }
                };
            L.control.layers(
                layer_control_1b84a12ae2f0444893b1237e17ca9823.base_layers,
                layer_control_1b84a12ae2f0444893b1237e17ca9823.overlays,
                {position: 'topright',
                 collapsed: true,
                 autoZIndex: true
                }).addTo(map_e9b6ee2bda63442881c2e83926db41bd);
        
</script>')