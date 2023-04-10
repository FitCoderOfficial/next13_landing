export async function fetchData() {
    const headers = {
        'X-RapidAPI-Key': 'affbec6919msh4a238971d067f54p107510jsne4de38976ad4',
        'X-RapidAPI-Host': 'cars-by-api-ninjas.p.rapidapi.com'
    }
    const response = await fetch('https://cars-by-api-ninjas.p.rapidapi.com/v1/cars?model=corolla', {
        headers: headers,
    });

    const result = await response.json();

    return result;
}