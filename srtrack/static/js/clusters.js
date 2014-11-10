function get_clusters(coord) 
{
    var arrCoord = [
	    [40.712264, -73.878937], 
	    [41.172840, 73.966827],
	    [40.810041, 73.983307] 
    ];

    var features = [];

    for (i=0; i < coord.length; i++)
    {
        var point = [parseFloat(coord[i][0]), parseFloat(coord[i][1])];
        var iconFeature = new ol.Feature({
            geometry: new ol.geom.Point(ol.proj.transform(point, 'EPSG:4326', 'EPSG:3857')), 
            name: '1'
        });
        features.push(iconFeature);
    }

    var source = new ol.source.Vector({ features: features });
    var clusterSource = new ol.source.Cluster({ distance: 20,source: source });
    var styleCache = {};
    var clusters = new ol.layer.Vector({
        source: clusterSource,
        style: function(feature, resolution) {
            var size = feature.get('features').length;
            var style = styleCache[size];
            if (!style) {
                style = [ new ol.style.Style({
                    image: new ol.style.Circle({
                        radius: 3,
                        stroke: new ol.style.Stroke({ color: '#000' }),
                        fill: new ol.style.Fill({ color: '#006600'})
                    })
                })];
                styleCache[size] = style;
            }
            return style;
        }
    }); // end style for green points

    return clusters;
}

function get_icons(coord) {
    var iconFeatures=[];

    console.log("pre");
    console.log(iconFeatures.length);

    for (i=0; i < coord.length; i++)
    {
        var point = [parseFloat(coord[i][0]), parseFloat(coord[i][1])];
        var iconFeature = new ol.Feature({
            geometry: new ol.geom.Point(ol.proj.transform(point, 'EPSG:4326', 'EPSG:3857')), 
            name: '1'
        });
        iconFeatures.push(iconFeature);
    }

    console.log("post");
    console.log(iconFeatures.length);
    
    var iconFeature2 = new ol.Feature({
        geometry: new ol.geom.Point(ol.proj.transform([-72.0704, 46.678], 'EPSG:4326', 'EPSG:3857')), 
        name: '1'
    });

    iconFeatures.push(iconFeature2);

    console.log("after");
    console.log(iconFeatures.length);
    
    //iconFeatures.push(iconFeature1);
    console.log("icom");
    console.log(iconFeatures.length);

    var vectorSource = new ol.source.Vector({
        features: iconFeatures
    });

    var circleStyle = new ol.style.Style({
        image: new ol.style.Circle({
            radius: 3,
            stroke: new ol.style.Stroke({ color: '#000' }),
            fill: new ol.style.Fill({ color: '#006600'}),
        }),
    });

    var vectorLayer = new ol.layer.Vector({
        source: vectorSource,
        style: circleStyle
    });

    return vectorLayer;
}