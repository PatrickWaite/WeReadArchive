def get_Query():
    query = """
    SELECT * 
    FROM FIVEC_CIRCHISTORY_OUT fco 
    WHERE LOAN_DATETIME >= TO_DATE('01/JUL/2021')
	AND LOAN_DATETIME <= TO_DATE('30/JUN/2022')
	AND Z30_SUB_LIBRARY LIKE 'UM%';
    """
    return query

def marcTabPull(list):
    query = f""" 
select 
	m."content" as "ISBN",
	it.title,
	m.instance_hrid,
	hrt.call_number,
	lt."name" as "Location",
	lt2."name" as "Campus",
    lt2.code as "CampusCode"
from 
	folio_source_record.marctab m 
	join inventory.instance__t it on it.hrid = m.instance_hrid 
	join inventory.holdings_record__t hrt on hrt.instance_id = it.id 
	join inventory.location__t lt on lt.id = hrt.effective_location_id 
	join inventory.loccampus__t lt2 on lt2.id = lt.campus_id 
where 
	m.field = '020'
	and 
	m.sf = 'a'
    and
    m.content in ({list})
    """
    return query

#"loc-campus__t".code = 'UM'