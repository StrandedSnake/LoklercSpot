import json, sys
with open(sys.argv[1]) as fp:
    data = json.load(fp)
p = data.get('colors', data)
def get(key):
    try:
        v = p[key]
        if isinstance(v, dict):
            v2 = v.get('default', v.get('dark', v))
            if isinstance(v2, dict): return v2.get('color', '#1e1e2e')
            return v2
        return v
    except: return '#1e1e2e'
result = {'base':get('background'),'mantle':get('surface'),'crust':get('surface_dim'),'text':get('on_background'),'subtext0':get('on_surface_variant'),'subtext1':get('on_surface'),'surface0':get('surface_container'),'surface1':get('surface_container_high'),'surface2':get('surface_container_highest'),'overlay0':get('outline'),'overlay1':get('outline_variant'),'overlay2':get('secondary'),'blue':get('primary'),'sapphire':get('tertiary'),'peach':get('secondary_container'),'green':get('tertiary_container'),'red':get('error'),'mauve':get('on_primary'),'pink':get('on_tertiary'),'yellow':get('on_secondary_container'),'maroon':get('on_error'),'teal':get('on_tertiary_container'),'primary':get('primary')}
with open(sys.argv[2], 'w') as fp:
    json.dump(result, fp, indent=4)
