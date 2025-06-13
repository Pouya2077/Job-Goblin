export type Job = {
    id: string, 
    title: string,
    jsonb: any,
    user_email: string,
    min_salary: number, 
    company: string, 
    location: Array<string>, 
    description: string,
}