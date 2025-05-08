import {createClient} from "@supabase/supabase-js"

export default createClient((process.env.SUPA_URL as string), (process.env.ANON_KEY as string));

