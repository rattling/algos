package analysis.java;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import javax.swing.*;
import java.awt.Dimension;

public class ScatterPlot extends JFrame {

    // Constructor now takes sizes and timings as arguments and creates the chart
    public ScatterPlot(String title, int[] sizes, long[] timings, boolean logScale) {
        super(title);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        if (logScale) {
            displayLog2SizeVsTimingChart(sizes, timings);
        } else {
            displaySizeVsTimingChart(sizes, timings);
        }
    }

    // Create the dataset for size vs timing scatter plot
    private XYSeriesCollection createDataset(int[] sizes, long[] timings) {
        XYSeries series = new XYSeries("Size vs Timing");
        for (int i = 0; i < sizes.length; i++) {
            series.add(sizes[i], timings[i]);
        }
        XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(series);
        return dataset;
    }

    // Create the dataset for log2(size) vs log2(timing) scatter plot
    private XYSeriesCollection createLogDataset(int[] sizes, long[] timings) {
        XYSeries series = new XYSeries("log2(Size) vs log2(Timing)");

        for (int i = 0; i < sizes.length; i++) {
            // Ensure values are greater than 0 to avoid illegal log computation
            if (sizes[i] > 0 && timings[i] > 0) {
                series.add(Math.log(sizes[i]) / Math.log(2), Math.log(timings[i]) / Math.log(2));
            } else {
                System.out.println("Skipping non-positive value at index " + i + ": size=" + sizes[i] + ", timing=" + timings[i]);
            }
        }

        XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(series);
        return dataset;
    }


    // Create chart
    private JFreeChart createChart(XYSeriesCollection dataset, String title, String xAxisLabel, String yAxisLabel) {
        return ChartFactory.createScatterPlot(
                title,
                xAxisLabel, yAxisLabel,
                dataset,
                PlotOrientation.VERTICAL,
                true, true, false);
    }

    // Display size vs timing scatter plot
    private void displaySizeVsTimingChart(int[] sizes, long[] timings) {
        XYSeriesCollection dataset = createDataset(sizes, timings);
        JFreeChart chart = createChart(dataset, "Size vs Timing", "Size", "Timing");

        ChartPanel chartPanel = new ChartPanel(chart);
        chartPanel.setPreferredSize(new Dimension(800, 600));
        setContentPane(chartPanel);
    }

    // Display log2(size) vs log2(timing) scatter plot
    private void displayLog2SizeVsTimingChart(int[] sizes, long[] timings) {
        XYSeriesCollection dataset = createLogDataset(sizes, timings);
        JFreeChart chart = createChart(dataset, "log2(Size) vs log2(Timing)", "log2(Size)", "log2(Timing)");

        ChartPanel chartPanel = new ChartPanel(chart);
        chartPanel.setPreferredSize(new Dimension(800, 600));
        setContentPane(chartPanel);
    }

    // You can remove the main method, since this is now handled by passing arrays externally
}
