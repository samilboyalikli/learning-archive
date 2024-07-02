import React, { useEffect, useRef } from 'react'
import { useSelector } from "react-redux";
import * as d3 from 'd3';

function Rate() {

    //-------------------------------------------------------------------------------------------------
    //ORAN TESPİTİNİN YAPILDIĞI ALAN
    //-------------------------------------------------------------------------------------------------

    const { booler } = useSelector(state => state.booler)
    const { secondBooler } = useSelector(state => state.secondBooler)
    const { thirdBooler } = useSelector(state => state.thirdBooler)
    const { fourthBooler } = useSelector(state => state.fourthBooler)
    const { fifthBooler } = useSelector(state => state.fifthBooler)
    const { sixthBooler } = useSelector(state => state.sixthBooler)
    const { seventhBooler } = useSelector(state => state.seventhBooler)
    const { eighthBooler } = useSelector(state => state.eighthBooler)
    const { ninthBooler } = useSelector(state => state.ninthBooler)
    const { tenthBooler } = useSelector(state => state.tenthBooler)
    const { eleventhBooler } = useSelector(state => state.eleventhBooler)
    const { twelfthBooler } = useSelector(state => state.twelfthBooler)
    const { thirteenthBooler } = useSelector(state => state.thirteenthBooler)
    const { fourteenthBooler } = useSelector(state => state.fourteenthBooler)
    const { fifteenthBooler } = useSelector(state => state.fifteenthBooler)
    const { sixteenthBooler } = useSelector(state => state.sixteenthBooler)
    const { seventeenthBooler } = useSelector(state => state.seventeenthBooler)
    const { eighteenthBooler } = useSelector(state => state.eighteenthBooler)
    const { nineteenthBooler } = useSelector(state => state.nineteenthBooler)
    const { twentiethBooler } = useSelector(state => state.twentiethBooler)

    const components = [
        booler, secondBooler, thirdBooler, fourthBooler, fifthBooler,
        sixthBooler, seventhBooler, eighthBooler, ninthBooler, tenthBooler,
        eleventhBooler, twelfthBooler, thirteenthBooler, fourteenthBooler, fifteenthBooler,
        sixteenthBooler, seventeenthBooler, eighteenthBooler, nineteenthBooler, twentiethBooler
    ]

    let trueCount = 0
    let falseCount = 0

    components.forEach(component => {
        if (component === true) {
            trueCount++
        } else {
            falseCount++
        }
    })

    console.log("True Sayısı: ", trueCount)
    console.log("False Sayısı: ", falseCount)


    //-------------------------------------------------------------------------------------------------
    //GRAFİĞİN OLUŞTURULDUĞU ALAN
    //-------------------------------------------------------------------------------------------------

    const chartRef = useRef(null);

    useEffect(() => {

        d3.select(chartRef.current).selectAll("*").remove();

        const data = [falseCount, trueCount]; // Veri
        const width = 400; // Grafik genişliği
        const height = 400; // Grafik yüksekliği
        const radius = Math.min(width, height) / 2; // Yarıçap

        const svg = d3.select(chartRef.current) // SVG öğesini seç
            .append('svg') // SVG öğesi ekle
            .attr('width', width)
            .attr('height', height)
            .append('g') // G öğesi ekle
            .attr('transform', `translate(${width / 2},${height / 2})`); // Merkezi hizala

        const color = d3.scaleOrdinal()
            .domain([0, 1])
            .range(['green', 'red']); // Renk paleti

        const pie = d3.pie()
            .value(d => d);

        const arc = d3.arc()
            .innerRadius(0)
            .outerRadius(radius);

        const arcs = svg.selectAll('arc')
            .data(pie(data))
            .enter()
            .append('g')
            .attr('class', 'arc');

        arcs.append('path')
            .attr('d', arc)
            .attr('fill', (d, i) => color(i));

        arcs.append('text')
            .attr('transform', d => `translate(${arc.centroid(d)})`)
            .attr('text-anchor', 'middle')
            .attr('font-size', '10px')
            .text(d => d.data);
    }, [falseCount, trueCount]);

    return (
        <div className='d-flex' style={{marginLeft: '13rem'}}>
            <div ref={chartRef}></div>
            <div className='d-flex align-items-center' style={{marginLeft: '2rem'}}>
                <div>
                    <div className="card bg-primary text-white mb-3" style={{width: '13rem'}}>
                        <div className="card-header">
                        BOŞ MASA SAYISI
                        </div>
                        <ul className="list-group list-group-flush">
                            <li className="list-group-item">{falseCount}</li>
                        </ul>
                    </div>
                    <div className="card bg-primary text-white" style={{width: '13rem'}}>
                        <div className="card-header">
                        DOLU MASA SAYISI
                        </div>
                        <ul className="list-group list-group-flush">
                            <li className="list-group-item">{trueCount}</li>
                        </ul>
                    </div>
                    </div>
                </div>
            </div>
            )
}

            export default Rate
